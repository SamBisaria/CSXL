import { Component, OnInit } from '@angular/core';
import {
  FormBuilder,
  FormControl,
  FormGroup,
  Validators
} from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ClientPostContent, ServerResponsePost } from '../news.model';
import { Observable } from 'rxjs';
import { Organization } from '../../organization/organization.model';
import { PermissionService } from '../../permission.service';
import { NewsService } from '../news.service';
import { NonNullAssert } from '@angular/compiler';
import { D } from '@angular/cdk/keycodes';
import { HttpResponse } from '@angular/common/http';

@Component({
  selector: 'app-news-create-post',
  templateUrl: './news-create-post.component.html',
  styleUrls: ['./news-create-post.component.css']
})
export class NewsCreatePostComponent {
  public static Route = {
    path: 'newsform/edit/:id',
    title: 'News Form',
    component: NewsCreatePostComponent
  };

  postForm = this.formBuilder.nonNullable.group({
    headline: new FormControl<string>('', [Validators.required]),
    synopsis: new FormControl<string>('', [Validators.required]),
    mainStory: new FormControl<string>('', [Validators.required]),
    imageURL: new FormControl<string>('', [Validators.required]),
    organization: new FormControl<number>(-1),
    announcement: new FormControl<boolean>(false, [Validators.required])!
  });
  postModel: ClientPostContent | undefined;
  public enabled$: Observable<boolean> | undefined;
  isNew: boolean = false;
  draftID = -1;
  lastSavedTime: String = '';

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
    this.isNew = this.route.snapshot.paramMap.get('id') === '-1';
    this.draftID = parseInt(
        <string>this.route.snapshot.paramMap.get('id')
      );
  }

  ngOnInit(): void {
    if (!this.isNew) {
      let draft = this.newsService.getDraftByID(this.draftID);
      if (draft === null) {
        // Show draft does not exist page
      } else {
        this.postForm.controls.headline.setValue(draft.headline);
        this.postForm.controls.synopsis.setValue(draft.synopsis);
        this.postForm.controls.mainStory.setValue(draft.main_story);
        this.postForm.controls.announcement.setValue(draft.announcement);
        this.postForm.controls.imageURL.setValue(draft.image_url);
      }
    }
    // this.postForm.get('headline')?.addValidators(Validators.required);
    // this.postForm.get('mainStory')?.addValidators(Validators.required);

    // synopsis: new FormControl(this.postModel?.synopsis),
    // organization: new FormControl(this.postModel?.organization_id),
    // announcement: new FormControl(this.postModel?.announcement),
    // category: new FormControl(this.postModel?.category)
  }

  previewPost() {}
  savePost() {
    this.lastSavedTime = new Date().toLocaleTimeString();
    let clientPostContent: ClientPostContent = {
      headline: <string>this.postForm.controls['headline'].value,
      synopsis: <string>this.postForm.controls['synopsis'].value,
      main_story: <string>this.postForm.controls['mainStory'].value,
      state: 'draft',
      image_url: <string>this.postForm.controls['imageURL'].value,
      announcement: Boolean(this.postForm.controls['announcement'].value),
      category: '',
      organization_id: 1
    };
    let httpResponseObservable: Observable<HttpResponse<ServerResponsePost>>;
    if (this.isNew) {
      httpResponseObservable = this.newsService.addPost(clientPostContent);
    } else {
      httpResponseObservable = this.newsService.updatePost(
        this.draftID,
        clientPostContent
      );
    }
    let x;
    // Shows success notification and then navigates away on success, otherwise shows error notification
    httpResponseObservable.subscribe((data) => {
      x = data;
      if (data.body == null) {
        // Request or Malformed Data error
      }
      if (data.ok) {
        console.log(200);
        this.router.navigate(['/newsform']);
      } else {
        // An error occured
      }
    });
    console.log(x);
  }
  submitPost(): void {
    this.savePost();
  }

  discardPost() {
    if (!this.isNew) {
      let httpResponseObservable: Observable<HttpResponse<ServerResponsePost>> = this.newsService.deleteDrafts(this.draftID);
      httpResponseObservable.subscribe((response) => {
        if (response.ok) {
          // TODO show successfully discarded popup menu
          this.router.navigate(['/newsform']);
        } else {
          // TODO show discard error
        }
      });
    }
  }
}
