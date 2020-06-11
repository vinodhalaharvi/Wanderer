import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ConnectHotelPage } from './connect-hotel.page';

const routes: Routes = [
  {
    path: '',
    component: ConnectHotelPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ConnectHotelPageRoutingModule {}
