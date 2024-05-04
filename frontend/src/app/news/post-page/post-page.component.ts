import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { NewsService } from '../news.service';
import { ServerResponsePost } from '../news.model';

@Component({
  selector: 'app-post-page',
  templateUrl: './post-page.component.html',
  styleUrls: ['./post-page.component.css']
})
export class PostPageComponent implements OnInit {
  public static Route = {
    path: 'news/:id',
    title: 'News',
    component: PostPageComponent
  };

  post: ServerResponsePost | null = null;

  constructor(
    private route: ActivatedRoute,
    private newsService: NewsService
  ) {}

  ngOnInit(): void {
    this.getPost();
  }

  getPost(): void {
    const id = parseInt(this.route.snapshot.paramMap.get('id') || '', 10);
    this.post = this.newsService.getPostByID(id!);
  }

  isImageLoadable(url: string): boolean {
    const img = new Image();
    img.src = url;
    img.onerror = () => false;
    img.onload = () => true;
    return img.complete;
  }
}
