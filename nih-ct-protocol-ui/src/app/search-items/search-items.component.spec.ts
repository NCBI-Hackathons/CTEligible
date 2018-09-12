import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchItemsComponent } from './search-items.component';

describe('SearchItemsComponent', () => {
  let component: SearchItemsComponent;
  let fixture: ComponentFixture<SearchItemsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SearchItemsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchItemsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
