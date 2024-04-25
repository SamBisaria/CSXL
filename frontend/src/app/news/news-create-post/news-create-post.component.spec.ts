import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NewsCreatePostComponent } from './news-create-post.component';

describe('NewsFormComponent', () => {
  let component: NewsCreatePostComponent;
  let fixture: ComponentFixture<NewsCreatePostComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [NewsCreatePostComponent]
    }).compileComponents();

    fixture = TestBed.createComponent(NewsCreatePostComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
