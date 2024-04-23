import { Component } from '@angular/core';
import { NewsService } from './news.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css']
})
export class NewsComponent {
  public static Route = {
    path: 'news',
    title: 'News',
    component: NewsComponent
  };

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    public newsService: NewsService
  ) {
    this.newsService.getAllPosts();
  }
}
