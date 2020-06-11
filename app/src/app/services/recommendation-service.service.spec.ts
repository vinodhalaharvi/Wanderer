import { TestBed } from '@angular/core/testing';

import { RecommendationServiceService } from './recommendation-service.service';

describe('RecommendationServiceService', () => {
  let service: RecommendationServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RecommendationServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
