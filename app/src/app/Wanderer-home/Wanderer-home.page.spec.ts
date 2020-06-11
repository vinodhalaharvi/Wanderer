import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { WandererHomePage } from './Wanderer-home.page';

describe('WandererHomePage', () => {
  let component: WandererHomePage;
  let fixture: ComponentFixture<WandererHomePage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WandererHomePage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(WandererHomePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
