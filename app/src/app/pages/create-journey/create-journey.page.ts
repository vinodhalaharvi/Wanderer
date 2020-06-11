import { Component, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { Router, NavigationExtras } from '@angular/router';

@Component({
  selector: 'app-create-journey',
  templateUrl: './create-journey.page.html',
  styleUrls: ['./create-journey.page.scss'],
})
export class CreateJourneyPage implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }

  createJourney()
  {
    let navigationExtras: NavigationExtras = {
      state: {
      }
    };
    this.router.navigate(['google-maps'], navigationExtras);
  }  

}
