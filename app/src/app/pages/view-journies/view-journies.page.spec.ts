import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { ViewJourniesPage } from './view-journies.page';

describe('ViewJourniesPage', () => {
  let component: ViewJourniesPage;
  let fixture: ComponentFixture<ViewJourniesPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ViewJourniesPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(ViewJourniesPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
