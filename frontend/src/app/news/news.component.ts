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
  public sortedPosts: any[] = [];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    public newsService: NewsService
  ) {
    this.newsService.refreshPosts();
    this.sortPosts();
  }

  protected readonly Array = Array;

  private sortPosts(): void {
    const posts = Array.from(this.newsService.posts.values());
    this.sortedPosts = posts.sort((a, b) => {
      if (a.announcement && !b.announcement) {
        return -1;
      } else if (!a.announcement && b.announcement) {
        return 1;
      } else {
        return (
          new Date(b.modified_timestamp).getTime() -
          new Date(a.modified_timestamp).getTime()
        );
      }
    });
  }
}
