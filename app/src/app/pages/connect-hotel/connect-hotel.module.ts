import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ConnectHotelPageRoutingModule } from './connect-hotel-routing.module';

import { ConnectHotelPage } from './connect-hotel.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ConnectHotelPageRoutingModule
  ],
  declarations: [ConnectHotelPage]
})
export class ConnectHotelPageModule {}
