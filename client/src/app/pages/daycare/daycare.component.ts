import { Component, ChangeDetectionStrategy } from '@angular/core';
import { OnInit } from '@angular/core/src/metadata/lifecycle_hooks';

@Component({
  selector: 'ngx-daycare',
  templateUrl: './daycare.component.html',
  styleUrls: ['./daycare.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DaycareComponent implements OnInit {

  public distance: number;
  public nombreEnfants: number;
  public prix: number;
  public isPublic: boolean;

  ngOnInit() {
    this.distance = 5;
    this.nombreEnfants = 1;
    this.prix = 8;
    this.isPublic = true;
  }
}
