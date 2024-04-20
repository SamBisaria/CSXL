import { Injectable } from '@angular/core';
import { Post, posts } from './news.model';

@Injectable({
  providedIn: 'root'
})
export class NewsService {
  newsPosts: Post[];
  nextID = 3;

  constructor() {
    this.newsPosts = posts;
    this.buildPost(-1, '', '', false);
  }

  getAllPosts(): Post[] {
    return this.newsPosts;
  }

  getAllPostsByDate(): Post[] {
    return this.newsPosts.sort((a, b) => {
      return b.publishDate.getTime() - a.publishDate.getTime();
    });
  }

  getID(): number {
    return this.nextID;
  }

  getPostById(id: number): Post | undefined {
    return this.newsPosts.find((post) => post.id === id);
  }

  public buildPost(
    id: number,
    headline: string,
    mainStory: string,
    announcement: boolean,
    synopsis?: string
  ) {
    if (headline === null || mainStory === null) {
      window.alert('Error: One or more fields is invalid!');
      return;
    }
    if (id === -1 || !this.getPostById(id)) {
      id = this.nextID;
      this.nextID++;
    }
    const postData: Post = {
      id,
      headline,
      mainStory,
      synopsis,
      author: '',
      state: 'Draft',
      slug: '',
      publishDate: new Date(),
      modificationDate: new Date(),
      announcement,
      upvotes: 0,
      downvotes: 0
    };

    if (
      this.getPostById(id) !== null &&
      this.getPostById(id) !== undefined &&
      id !== -1
    ) {
      this.updatePost(postData);
    } else {
      this.addPost(postData);
    }
  }

  addPost(newPost: Post): void {
    this.newsPosts.push(newPost);
  }

  deletePost(id: number): void {
    this.newsPosts = this.newsPosts.filter((post) => post.id !== id);
  }

  updatePost(updatedPost: Post): void {
    const index = this.newsPosts.findIndex(
      (post) => post.id === updatedPost.id
    );
    if (index !== -1) {
      this.newsPosts[index] = updatedPost;
    }
  }
}
