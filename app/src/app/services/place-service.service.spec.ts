import { TestBed } from '@angular/core/testing';

import { PlaceServiceService } from './place-service.service';

describe('PlaceServiceService', () => {
  let service: PlaceServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PlaceServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
