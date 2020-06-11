import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { ConnectHotelPage } from './connect-hotel.page';

describe('ConnectHotelPage', () => {
  let component: ConnectHotelPage;
  let fixture: ComponentFixture<ConnectHotelPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ConnectHotelPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(ConnectHotelPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
