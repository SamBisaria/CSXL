import { Component } from '@angular/core';
import { NewsWidgetComponent } from '../news/news-widget/news-widget.widget';
import { NewsService } from '../news/news.service';

@Component({
  selector: 'app-news-drafts',
  templateUrl: './news-drafts.component.html',
  styleUrls: ['./news-drafts.component.css']
})
export class NewsDraftsComponent {
  public static Route = {
    path: 'newsform',
    title: 'News Form',
    component: NewsDraftsComponent
  };
  constructor(public newsService: NewsService) {}
}
