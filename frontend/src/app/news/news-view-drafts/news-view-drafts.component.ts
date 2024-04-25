import { Component } from '@angular/core';
import { NewsWidgetComponent } from '../widgets/view-post/view-post.widget';
import { NewsService } from '../news.service';

@Component({
  selector: 'app-news-view-drafts',
  templateUrl: './news-view-drafts.component.html',
  styleUrls: ['./news-view-drafts.component.css']
})
export class NewsViewDraftsComponent {
  public static Route = {
    path: 'newsform',
    title: 'News Drafts',
    component: NewsViewDraftsComponent
  };
  constructor(public newsService: NewsService) {
    this.newsService.refreshDrafts();
  }

  protected readonly Array = Array;
}
