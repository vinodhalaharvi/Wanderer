import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ViewJourniesPage } from './view-journies.page';

const routes: Routes = [
  {
    path: '',
    component: ViewJourniesPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ViewJourniesPageRoutingModule {}
