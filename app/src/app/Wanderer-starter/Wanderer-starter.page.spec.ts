import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { WandererStarterPage } from './Wanderer-starter.page';

describe('WandererStarterPage', () => {
  let component: WandererStarterPage;
  let fixture: ComponentFixture<WandererStarterPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WandererStarterPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(WandererStarterPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
