import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { WandererLoginPageRoutingModule } from './Wanderer-login-routing.module';

import { WandererLoginPage } from './Wanderer-login.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    WandererLoginPageRoutingModule
  ],
  declarations: [WandererLoginPage]
})
export class WandererLoginPageModule {}
