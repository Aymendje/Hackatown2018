import { Component, ChangeDetectionStrategy } from '@angular/core';
import { OnInit } from '@angular/core/src/metadata/lifecycle_hooks';

@Component({
  selector: 'ngx-sports',
  templateUrl: './sports.component.html',
  styleUrls: ['./sports.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SportsComponent implements OnInit {

  public distance: number;
  public nombreEnfants: number;
  public prix: number;
  public isPublic: boolean;

  public daycares: Array<any>;

  ngOnInit() {
    this.initialize();
  }

  private initialize() {
    this.distance = 5;
    this.nombreEnfants = 1;
    this.prix = 8;
    this.isPublic = true;

    this.daycares = [
      {
        name: "Garderie du bonheur",
        distance: 5,
        price: 12,
        description: "Situé proche d'une école primaire et facilement accessible via l'autoroute 20, la Garderie du bonheur est la garderie parfaite pour les budgets moyens",
        available: 20
      },
      {
        name: "jbdfuqvdfyig",
        distance: 7.5,
        price: 9,
        description: "Situé proche d'une école primaire et facilement accessible via l'autoroute 20, la Garderie du bonheur est la garderie parfaite pour les budgets moyens",
        available: 6
      }
    ];
  }

  public query() {
    // Calling the web service
    alert("query");
  }
}
