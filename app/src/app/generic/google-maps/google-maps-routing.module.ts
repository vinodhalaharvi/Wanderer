import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { GoogleMapsPage } from './google-maps.page';

const routes: Routes = [
  {
    path: '',
    component: GoogleMapsPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class GoogleMapsPageRoutingModule {}
