import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {CommonModule, NgOptimizedImage} from '@angular/common';

/* HTTP and Auth */
import { RouterModule } from '@angular/router';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { HttpRequestInterceptor } from './navigation/http-request.interceptor';
import { JwtModule } from '@auth0/angular-jwt';

/* UI / Material Dependencies */
import { DatePipe, NgForOf } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { LayoutModule } from '@angular/cdk/layout';

/* Material UI Dependencies */
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatDialogModule } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatListModule } from '@angular/material/list';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatSliderModule } from '@angular/material/slider';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatTabsModule } from '@angular/material/tabs';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatStepperModule } from '@angular/material/stepper';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatCheckboxModule } from '@angular/material/checkbox';

/* Application Specific */
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavigationComponent } from './navigation/navigation.component';
import { SlackInviteBox } from './navigation/widgets/slack-invite-box/slack-invite-box.widget';
import { ErrorDialogComponent } from './navigation/error-dialog/error-dialog.component';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { GateComponent } from './gate/gate.component';
import { SharedModule } from './shared/shared.module';
import { NewsComponent } from './news/news.component';
import { NewsCreatePostComponent } from './news/news-create-post/news-create-post.component';
import { NewsViewDraftsComponent } from './news/news-view-drafts/news-view-drafts.component';
import { NewsWidgetComponent } from './news/widgets/view-post/view-post.widget';
import { NewsFrontPageComponent } from './news/news-front-page/news-front-page.component';
import { PostWidget } from './news/widgets/post-widget/post-widget.widget';
import { EditorModule, TINYMCE_SCRIPT_SRC } from '@tinymce/tinymce-angular';
import { ToastrModule } from 'ngx-toastr';
import { PostPageComponent } from './news/post-page/post-page.component';

@NgModule({
  declarations: [
    AppComponent,
    NavigationComponent,
    SlackInviteBox,
    ErrorDialogComponent,
    HomeComponent,
    AboutComponent,
    GateComponent,
    NewsComponent,
    NewsCreatePostComponent,
    NewsViewDraftsComponent,
    NewsWidgetComponent,
    NewsFrontPageComponent,
    PostWidget,
    PostPageComponent
  ],
    imports: [
        /* Angular */
        BrowserModule,
        BrowserAnimationsModule,
        HttpClientModule,
        NgForOf,
        AppRoutingModule,
        LayoutModule,
        ReactiveFormsModule,
        CommonModule,

        /* Material UI */
        MatButtonModule,
        MatCardModule,
        MatDialogModule,
        MatFormFieldModule,
        MatIconModule,
        MatInputModule,
        MatListModule,
        MatProgressBarModule,
        MatSidenavModule,
        MatSliderModule,
        MatSnackBarModule,
        MatStepperModule,
        MatTabsModule,
        MatToolbarModule,
        MatTooltipModule,
        MatCheckboxModule,
        FormsModule,
        RouterModule,
        SharedModule,
        JwtModule.forRoot({
            config: {
                tokenGetter: () => {
                    return localStorage.getItem('bearerToken');
                }
            }
        }),
        EditorModule, // Fancy Markdown Editing
        BrowserAnimationsModule, // Notifications
        ToastrModule.forRoot(),
        NgOptimizedImage
    ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: HttpRequestInterceptor,
      multi: true
    },
    DatePipe,
    { provide: TINYMCE_SCRIPT_SRC, useValue: 'tinymce/tinymce.min.js' }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
