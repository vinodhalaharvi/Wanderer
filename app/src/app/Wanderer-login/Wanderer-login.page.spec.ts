import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { WandererLoginPage } from './Wanderer-login.page';

describe('WandererLoginPage', () => {
  let component: WandererLoginPage;
  let fixture: ComponentFixture<WandererLoginPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WandererLoginPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(WandererLoginPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
