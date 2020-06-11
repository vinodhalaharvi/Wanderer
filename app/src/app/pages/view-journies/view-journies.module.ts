import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ViewJourniesPageRoutingModule } from './view-journies-routing.module';

import { ViewJourniesPage } from './view-journies.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ViewJourniesPageRoutingModule
  ],
  declarations: [ViewJourniesPage]
})
export class ViewJourniesPageModule {}
