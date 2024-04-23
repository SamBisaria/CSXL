import { Component, EventEmitter, Input, Output, OnInit } from '@angular/core';
import { Post } from '../news.model';
import { NewsService } from '../news.service';
import { Router } from '@angular/router';

@Component({
  selector: 'post-widget',
  templateUrl: './post-widget.widget.html',
  styleUrls: ['./post-widget.widget.css']
})
export class PostWidget {
  /** Inputs and outputs go here */
  @Input() post!: Post;
  /** Constructor */
  constructor(
    public newsService: NewsService,
    private router: Router
  ) {}
  titleLink() {
    this.router.navigate(['/get', this.post.id]);
  }
}
