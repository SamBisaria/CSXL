import { Component } from '@angular/core';

@Component({
  selector: 'app-news-front-page',
  templateUrl: './news-front-page.component.html',
  styleUrls: ['./news-front-page.component.css']
})
export class NewsFrontPageComponent {
  public static Route = {
    path: 'news/:id',
    title: 'News',
    component: NewsFrontPageComponent
  };

  constructor() {}
}
