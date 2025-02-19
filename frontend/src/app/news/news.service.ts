import { Injectable } from '@angular/core';
import { ClientPostContent, ServerResponsePost } from './news.model';
import { Observable, OperatorFunction, ReplaySubject, map } from 'rxjs';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NewsService {
  posts: Map<number, ServerResponsePost> = new Map<
    number,
    ServerResponsePost
  >();
  drafts: Map<number, ServerResponsePost> = new Map<
    number,
    ServerResponsePost
  >();

  // private newsPosts: ReplaySubject<Map<number,ServerResponsePost>> = new ReplaySubject(1);
  // newsPosts$: Observable<Map<number,ServerResponsePost>> = this.newsPosts.asObservable();
  //newsPosts: Post[];
  nextID = null;

  constructor(protected http: HttpClient) {}
  // We need to add getAllDrafts() and other equivalents for drafts, and replace these post things
  refreshPosts() {
    this.http
      .get<ServerResponsePost[]>('/api/news/get')
      .subscribe((postsList) => {
        this.posts.clear();
        for (let i = 0; i < postsList.length; i++) {
          this.posts.set(postsList[i].id, postsList[i]);
        }
      });
  }
  refreshDrafts() {
    this.http
      .get<ServerResponsePost[]>('/api/news/draft/get')
      .subscribe((draftList) => {
        this.drafts.clear();
        for (let i = 0; i < draftList.length; i++) {
          this.drafts.set(draftList[i].id, draftList[i]);
        }
      });
  }

  // getAllPostsByDate() {
  //   this.http
  //     .get<ServerResponsePost[]>('/api/news/date')
  //     .subscribe((posts) => this.newsPosts.next(posts));
  // }

  // getID() {
  //   return this.nextID;
  // }

  getDraftByID(id: number): ServerResponsePost | null {
    let draft = this.drafts.get(id);
    if (draft === undefined) {
      return null;
    }
    return draft;
    // let x = this.drafts.get(id);
    // if (x === undefined) {
    //   return null;
    // } else {
    //   return of(<HttpResponse<ServerResponsePost>{
    //     ok: true,
    //     body: x
    //   });
    // }

    // No need to make a slow HTTP call when we can just wrap the local value as an observable.
    // return this.http.get<ServerResponsePost>('/api/news/get/' + id);
  }

  getPostByID(id: number): ServerResponsePost | null {
    let post = this.posts.get(id);
    if (post === undefined) {
      return null;
    }
    return post;
  }
  // if (id === -1 || !this.getPostById(id)) {
  //   id = this.nextID;
  //   this.nextID++;
  // }
  // } else {
  //   this.updatePost(postData).subscribe((put) => {});
  // }

  addPost(newPost: ClientPostContent): Observable<HttpResponse<any>> {
    return this.http.post<HttpResponse<ServerResponsePost>>(
      '/api/news/draft/post',
      newPost,
      { observe: 'response' }
    );
  }

  deleteDrafts(id: number): Observable<HttpResponse<any>> {
    this.drafts.delete(id);
    return this.http.delete(`/api/news/delete/${id}`, { observe: 'response' });
  }

  updatePost(
    postID: number,
    updatedPost: ClientPostContent
  ): Observable<HttpResponse<any>> {
    return this.http.put<ServerResponsePost>(
      `/api/news/draft/edit/${postID}`,
      updatedPost,
      { observe: 'response' }
    );
  }

  // private mapTimerResponseListToDataList: OperatorFunction<ServerResponsePost[], ClientPostContent[]> =
  //   map((responses) =>
  //     responses.map((response) => this.postResponseToData(response))
  //   );

  // private mapPostResponseToData: OperatorFunction<ServerResponsePost, ClientPostContent> = map(
  //   this.postResponseToData
  // );

  // postResponseToData(response: ServerResponsePost): ClientPostContent {
  //   return {
  //     id: response.id,
  //     headline: response.headline,
  //     synopsis: response.synopsis || '', // Optional property with default value
  //     main_story: response.main_story,
  //     author: response.author,
  //     state: response.state,
  //     slug: response.slug,
  //     published_timestamp: response.published_timestamp,
  //     last_modified_timestamp: response.last_modified_timestamp,
  //     mod_date: response.mod_date,
  //     announcement: response.announcement,
  //     category: response.category || '', // Optional property with default value
  //     upvotes: response.upvotes,
  //     downvotes: response.downvotes,
  //     organization_id: response.organization_id || 1
  //     // Optional property with default value
  //   };
  // }
}
