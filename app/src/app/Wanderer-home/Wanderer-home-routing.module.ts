import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { WandererHomePage } from './Wanderer-home.page';


const routes: Routes = [
    {
    path: 'home',
    component: WandererHomePage,
    children: [
      {
        path: 'create',
        loadChildren: () => import('../pages/create-journey/create-journey.module').then(m => m.CreateJourneyPageModule)
      },
      {
        path: 'view',
        loadChildren: () => import('../pages/view-journies/view-journies.module').then(m => m.ViewJourniesPageModule)
      },
      {
        path: 'connect',
        loadChildren: () => import('../pages/connect-hotel/connect-hotel.module').then(m => m.ConnectHotelPageModule)
      },
      {
        path: '',
        redirectTo: '/home/create',
        pathMatch: 'full'
      }
    ]
  },
  {
    path: '',
    redirectTo: '/home/create',
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class WandererHomePageRoutingModule {}
