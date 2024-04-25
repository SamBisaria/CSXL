import { Component, EventEmitter, Input, Output, OnInit } from '@angular/core';
import { ServerResponsePost } from '../../news.model';
import { NewsService } from '../../news.service';
import {HttpResponse} from "@angular/common/http";

@Component({
  selector: 'app-view-post',
  templateUrl: './view-post.widget.html',
  styleUrls: ['./view-post.widget.css']
})
export class NewsWidgetComponent {
  @Input() post!: ServerResponsePost;
  constructor(private newsService: NewsService) {}
  deletePost(id: number) {
    let x: HttpResponse<any>;
    this.newsService.deleteDrafts(id).subscribe((response) => {
      if (response.ok) {
        console.log("yay") // SHow successuflly deleted banner
      } else {
        console.log('boooo'); // Show deletion error
      }
    });
    // this.newsService.refreshPosts();
  }

  protected timeSincePostUpdated(): string {
    let currentTimeStamp = (Date.now() / 1000) | 0;
    let secondsSincePost = currentTimeStamp - this.post.modified_timestamp;
    if (secondsSincePost < 60) {
      return (secondsSincePost | 0) + ' seconds ago';
    } else if (secondsSincePost < 3600) {
      return ((secondsSincePost / 60) | 0) + ' minutes ago';
    } else if (secondsSincePost < 86400) {
      return ((secondsSincePost / 3600) | 0) + (secondsSincePost < 7200 ? ' hour ago' : ' hours ago');
    } else if (secondsSincePost < 2592000) {
      return ((secondsSincePost / 86400) | 0) + (secondsSincePost < 86400 * 2 ? ' day ago': ' days ago');
    } else if ((secondsSincePost < 31557600)) {
      return ((secondsSincePost / 2592000) | 0) + (secondsSincePost < 2592000 * 2 ? ' month ago' : ' months ago');
    } else {
      return ((secondsSincePost / 315576000) | 0) + ' years ago';
    }
  }
}
