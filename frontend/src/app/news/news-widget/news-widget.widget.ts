import { Component, EventEmitter, Input, Output, OnInit } from '@angular/core';
import { Post } from '../news.model';

@Component({
  selector: 'app-news-widget',
  templateUrl: './news-widget.widget.html',
  styleUrls: ['./news-widget.widget.css']
})
export class NewsWidgetComponent {
  @Input() post!: Post;
}
