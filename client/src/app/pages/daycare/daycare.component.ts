import { Component, ChangeDetectionStrategy, ChangeDetectorRef } from '@angular/core';
import { OnInit } from '@angular/core/src/metadata/lifecycle_hooks';
import { IDayCare } from './../../../../../common/models/daycare';
import { DayCareService } from './daycare.service';
import { DayCareViewModel } from './daycare.viewmodel';
import { Observable } from 'rxjs/Observable';

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
    public daycares: DayCareViewModel[];
    
    private location = {
        lat: 45.630692,
        long: -72.956329
    }

    constructor(private daycareService: DayCareService, private cd: ChangeDetectorRef) {
        
    }
    
    ngOnInit() {
        this.initialize();
    }
    
    private initialize() {
        this.distance = 5;
        this.nombreEnfants = 1;
        this.prix = 8;
    }
    
    public query() {
        this.daycareService.getDayCares(this.distance, this.prix, this.nombreEnfants, this.location.lat, this.location.long).then((result) => {
            this.daycares = [];
            for (let daycare of result) {
                let x = {
                    name: daycare.name,
                    price: daycare.price,
                    available: daycare.available,
                    description: "",
                    distance: this.calculateDistance(this.location.lat, this.location.long, daycare.location.lat, daycare.location.lng).toFixed(1)
                }
                this.daycares.push(x as DayCareViewModel);
            }
            this.cd.markForCheck();
        });
    }
    
    private calculateDistance(lat1:number, long1:number, lat2:number, long2:number) : number {
        let p = 0.017453292519943295;    // Math.PI / 180
        let c = Math.cos;
        let a = 0.5 - c((lat1-lat2) * p) / 2 + c(lat2 * p) *c((lat1) * p) * (1 - c(((long1- long2) * p))) / 2;
        let dis = (12742 * Math.asin(Math.sqrt(a))); // 2 * R; R = 6371 km
        return dis;
    }
}
