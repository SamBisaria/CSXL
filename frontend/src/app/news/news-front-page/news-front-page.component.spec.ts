import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NewsFrontPageComponent } from './news-front-page.component';

describe('NewsPageComponent', () => {
  let component: NewsFrontPageComponent;
  let fixture: ComponentFixture<NewsFrontPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NewsFrontPageComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NewsFrontPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
