import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { CreateJourneyPage } from './create-journey.page';

describe('CreateJourneyPage', () => {
  let component: CreateJourneyPage;
  let fixture: ComponentFixture<CreateJourneyPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateJourneyPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(CreateJourneyPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
