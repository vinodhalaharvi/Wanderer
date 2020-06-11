import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { CreateJourneyPageRoutingModule } from './create-journey-routing.module';

import { CreateJourneyPage } from './create-journey.page';


@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    CreateJourneyPageRoutingModule
  ],
  declarations: [CreateJourneyPage]
})
export class CreateJourneyPageModule {}
