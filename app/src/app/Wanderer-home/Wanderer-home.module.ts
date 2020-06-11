import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { WandererHomePageRoutingModule } from './Wanderer-home-routing.module';

import { WandererHomePage } from './Wanderer-home.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    WandererHomePageRoutingModule
  ],
  declarations: [WandererHomePage]
})
export class WandererHomePageModule {}
