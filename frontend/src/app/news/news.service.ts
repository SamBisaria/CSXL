import { Injectable } from '@angular/core';
import { Post, BackPost } from './news.model';
import { Observable, OperatorFunction, ReplaySubject, map } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class NewsService {
  private newsPosts: ReplaySubject<Post[]> = new ReplaySubject(1);
  newsPosts$: Observable<Post[]> = this.newsPosts.asObservable();
  //newsPosts: Post[];
  nextID = null;

  constructor(protected http: HttpClient) {
    this.newsPosts.next([]);
  }
  // We need to add getAllDrafts() and other equivalents for drafts, and replace these post things
  getAllPosts() {
    this.http
      .get<Post[]>('/api/news/get')
      .pipe(this.mapTimerResponseListToDataList)
      .subscribe((posts) => this.newsPosts.next(posts));
  }
  getAllDrafts() {
    this.http
      .get<Post[]>('/api/news/draft/get')
      .pipe(this.mapTimerResponseListToDataList)
      .subscribe((posts) => this.newsPosts.next(posts));
  }

  getAllPostsByDate() {
    this.http
      .get<Post[]>('/api/news/date')
      .pipe(this.mapTimerResponseListToDataList)
      .subscribe((posts) => this.newsPosts.next(posts));
  }

  getID() {
    return this.nextID;
  }

  getPostById(id: number): Observable<Post> {
    return this.http
      .get<BackPost>('/api/news/get/' + id)
      .pipe(this.mapPostResponseToData);
  }

  public buildPost(
    id: number | null,
    headline: string,
    mainStory: string,
    announcement: boolean,
    synopsis?: string
  ) {
    if (headline === null || mainStory === null) {
      window.alert('Error: One or more fields is invalid!');
      return;
    }
    // if (id === -1 || !this.getPostById(id)) {
    //   id = this.nextID;
    //   this.nextID++;
    // }
    const postData: Post = {
      id,
      headline,
      synopsis,
      main_story: mainStory,
      author: 0,
      slug: '',
      state: 'Draft',
      image_url: '',
      publish_date: '',
      mod_date: '',
      announcement: announcement || false,
      category: '',
      upvotes: 0,
      downvotes: 0,
      organization_id: 1
    };
    if (id === null) {
      this.addPost(postData).subscribe((post) => {});
    } else {
      this.updatePost(postData).subscribe((put) => {});
    }
  }

  addPost(newPost: Post): Observable<Post> {
    return this.http.post<Post>('/api/news/draft/post', newPost);
  }

  deletePost(id: number): Observable<any> {
    return this.http.delete(`/api/news/delete/${id}`);
  }

  updatePost(updatedPost: Post): Observable<Post> {
    return this.http
      .put<BackPost>('/api/news/draft/edit', updatedPost)
      .pipe(this.mapPostResponseToData);
  }

  private mapTimerResponseListToDataList: OperatorFunction<BackPost[], Post[]> =
    map((responses) =>
      responses.map((response) => this.postResponseToData(response))
    );

  private mapPostResponseToData: OperatorFunction<BackPost, Post> = map(
    this.postResponseToData
  );

  postResponseToData(response: BackPost): Post {
    return {
      id: response.id,
      headline: response.headline,
      synopsis: response.synopsis || '', // Optional property with default value
      main_story: response.main_story,
      author: response.author,
      state: response.state,
      slug: response.slug,
      publish_date: response.publish_date,
      mod_date: response.mod_date,
      announcement: response.announcement,
      category: response.category || '', // Optional property with default value
      upvotes: response.upvotes,
      downvotes: response.downvotes,
      organization_id: response.organization_id || 1
      // Optional property with default value
    };
  }
}
