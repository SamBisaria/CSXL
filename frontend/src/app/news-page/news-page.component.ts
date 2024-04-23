import { Component } from '@angular/core';

@Component({
  selector: 'app-news-page',
  templateUrl: './news-page.component.html',
  styleUrls: ['./news-page.component.css']
})
export class NewsPageComponent {
  public static Route = {
    path: 'news/:id',
    title: 'News',
    component: NewsPageComponent
  };

  constructor() {}
}
