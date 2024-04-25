import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NewsViewDraftsComponent } from './news-view-drafts.component';

describe('NewsDraftsComponent', () => {
  let component: NewsViewDraftsComponent;
  let fixture: ComponentFixture<NewsViewDraftsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NewsViewDraftsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NewsViewDraftsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
