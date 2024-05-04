import { Component, EventEmitter, Input, Output, OnInit } from '@angular/core';
import { ServerResponsePost } from '../../news.model';
import { NewsService } from '../../news.service';
import { HttpResponse } from '@angular/common/http';
import { ToastrService } from 'ngx-toastr';
import {state} from "@angular/animations";

@Component({
  selector: 'app-view-post',
  templateUrl: './view-post.widget.html',
  styleUrls: ['./view-post.widget.css']
})
export class NewsWidgetComponent {
  @Input() post!: ServerResponsePost;
  constructor(
    private newsService: NewsService,
    private toastr: ToastrService
  ) {}
  deletePost(id: number) {
    let x: HttpResponse<any>;
    this.newsService.deleteDrafts(id).subscribe((response) => {
      if (response.ok) {
        this.toastr.success('Draft Deleted', 'Success', { closeButton: true });
      } else {
        this.toastr.error('Failed to Delete Draft', 'Error', {
          closeButton: true
        });
      }
    });
    // this.newsService.refreshPosts();
  }

  protected timeSincePostUpdated(): string {
    let currentTimeStamp = (Date.now() / 1000) | 0;
    let secondsSincePost = currentTimeStamp - this.post.modified_timestamp;
    if (secondsSincePost < 60) {
      return (
        (secondsSincePost | 0) +
        (secondsSincePost > 0 && secondsSincePost < 2
          ? ' second ago'
          : ' seconds ago')
      );
    } else if (secondsSincePost < 3600) {
      return (
        ((secondsSincePost / 60) | 0) +
        (secondsSincePost < 120 ? ' minute ago' : ' minutes ago')
      );
    } else if (secondsSincePost < 86400) {
      return (
        ((secondsSincePost / 3600) | 0) +
        (secondsSincePost < 7200 ? ' hour ago' : ' hours ago')
      );
    } else if (secondsSincePost < 2592000) {
      return (
        ((secondsSincePost / 86400) | 0) +
        (secondsSincePost < 172800 ? ' day ago' : ' days ago')
      );
    } else if (secondsSincePost < 31557600) {
      return (
        ((secondsSincePost / 2592000) | 0) +
        (secondsSincePost < 5184000 ? ' month ago' : ' months ago')
      );
    } else {
      return (
        ((secondsSincePost / 315576000) | 0) +
        (secondsSincePost < 631152000 ? ' year ago' : ' years ago')
      );
    }
  }
  isImageLoadable(url: string): boolean {
    const img = new Image();
    img.src = url;
    img.onerror = () => false;
    img.onload = () => true;
    return img.complete;
  }

  protected readonly state = state;
}
