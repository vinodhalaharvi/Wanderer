import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { WandererLoginPage } from './Wanderer-login.page';

const routes: Routes = [
  {
    path: '',
    component: WandererLoginPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class WandererLoginPageRoutingModule {}
