import { Component, EventEmitter, Input, Output, OnInit } from '@angular/core';
import { Post } from '../news.model';
import { NewsService } from '../news.service';

@Component({
  selector: 'app-news-widget',
  templateUrl: './news-widget.widget.html',
  styleUrls: ['./news-widget.widget.css']
})
export class NewsWidgetComponent {
  @Input() post!: Post;
  constructor(public newsService: NewsService) {}
  deletePost(id: number) {
    this.newsService.deletePost(id).subscribe(() => {});
    this.newsService.getAllPosts();
  }
}
