import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { WandererStarterPageRoutingModule } from './Wanderer-starter-routing.module';

import { WandererStarterPage } from './Wanderer-starter.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    WandererStarterPageRoutingModule
  ],
  declarations: [WandererStarterPage]
})
export class WandererStarterPageModule {}
