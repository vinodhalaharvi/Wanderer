import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { WandererStarterPage } from './Wanderer-starter.page';

const routes: Routes = [
  {
    path: '',
    component: WandererStarterPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class WandererStarterPageRoutingModule {}
