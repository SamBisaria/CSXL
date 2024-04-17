import { Component, OnInit } from '@angular/core';
import {
  FormBuilder,
  FormControl,
  FormGroup,
  Validators
} from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Post } from '../news/news.model';
import { Observable } from 'rxjs';
import { Profile, PublicProfile } from '../profile/profile.service';
import { Organization } from '../organization/organization.model';
import { PermissionService } from '../permission.service';
import { NewsService } from '../news/news.service';

@Component({
  selector: 'app-news-form',
  templateUrl: './news-form.component.html',
  styleUrls: ['./news-form.component.css']
})
export class NewsFormComponent {
  public static Route = {
    path: 'newsform/edit/:id',
    title: 'News Form',
    component: NewsFormComponent
  };

  //implements oninit
  postForm: FormGroup | undefined;
  postModel: Post | undefined;
  public enabled$: Observable<boolean> | undefined;

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    public newsService: NewsService
  ) {
    // this.enabled$ = this.permission
    //   .check(
    //     'organization.events.update',
    //     `organization/${this.organization!.id}`
    //   )
    //   .pipe(map((permission) => permission || this.profile?.role === 'admin'));
  }

  ngOnInit(): void {
    const routeParams = this.route.snapshot.paramMap;
    const newsIdFromRoute = routeParams.get('id');
    if (newsIdFromRoute != null) {
      this.postModel = this.newsService.getPostById(parseInt(newsIdFromRoute));
    } else {
      this.postModel = this.newsService.getPostById(-1);
    }
    this.postForm = this.formBuilder.group({
      headline: new FormControl(
        this.postModel?.headline ?? '',
        Validators.required
      ),
      synopsis: new FormControl(this.postModel?.synopsis),
      mainStory: new FormControl(
        this.postModel?.mainStory ?? '',
        Validators.required
      ),
      organization: new FormControl(this.postModel?.organization),
      announcement: new FormControl(this.postModel?.announcement),
      category: new FormControl(this.postModel?.category)
    });
  }

  previewPost() {}
  savePost() {
    this.d = new Date();
    this.currentTime = this.d.toLocaleTimeString();
    let id = this.postModel?.id;
    if (!id || id === -1) {
      id = this.newsService.getID();
    }
    this.newsService.buildPost(
      id,
      this.postForm?.controls['headline'].value,
      this.postForm?.controls['mainStory'].value,
      this.postForm?.controls['announcement'].value,
      this.postForm?.controls['synopsis'].value
    );
  }
  submitPost(): void {
    this.savePost();
    this.router.navigate(['/news']);
  }
  d = new Date();
  currentTime = this.d.toLocaleTimeString();
}
