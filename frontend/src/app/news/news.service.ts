import { Injectable } from '@angular/core';
import { Post, posts } from './news.model';

@Injectable({
  providedIn: 'root'
})
export class NewsService {
  newsPosts: Post[] = posts;
  constructor() {}
}
