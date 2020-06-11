import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
   path: '',
    loadChildren: () => import('./Wanderer-home/Wanderer-home.module').then( m => m.WandererHomePageModule)
  },
  {
    path: 'Wanderer-starter',
    loadChildren: () => import('./Wanderer-starter/Wanderer-starter.module').then( m => m.WandererStarterPageModule)
  },
  {
    path: 'Wanderer-login',
    loadChildren: () => import('./Wanderer-login/Wanderer-login.module').then( m => m.WandererLoginPageModule)
  },
  {
    path: 'create-journey',
    loadChildren: () => import('./pages/create-journey/create-journey.module').then( m => m.CreateJourneyPageModule)
  },
  {
    path: 'view-journies',
    loadChildren: () => import('./pages/view-journies/view-journies.module').then( m => m.ViewJourniesPageModule)
  },
  {
    path: 'connect-hotel',
    loadChildren: () => import('./pages/connect-hotel/connect-hotel.module').then( m => m.ConnectHotelPageModule)
  },
  {
    path: 'google-maps',
    loadChildren: () => import('./generic/google-maps/google-maps.module').then( m => m.GoogleMapsPageModule)
  }
];
@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
