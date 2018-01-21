import { Component, ChangeDetectionStrategy } from '@angular/core';
import { OnInit } from '@angular/core/src/metadata/lifecycle_hooks';
import { IDayCare } from './../../../../../common/models/daycare';
import { DayCareService } from './daycare.service';
import { DayCareViewModel } from './daycare.viewmodel';

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
    
    public daycares: Array<DayCareViewModel>;
    private location: {
        lat: 45.6307,
        long: -72.9563
    }

    constructor(private daycareService: DayCareService) {
        
    }
    
    ngOnInit() {
        this.initialize();
    }
    
    private initialize() {
        this.distance = 5;
        this.nombreEnfants = 1;
        this.prix = 8;
        this.isPublic = true;
        
        this.daycares = new Array();
        this.daycares = [
            {
                name: "Garderie du bonheur",
                distance: 5,
                price: 12,
                description: "Situé proche d'une école primaire et facilement accessible via l'autoroute 20, la Garderie du bonheur est la garderie parfaite pour les budgets moyens",
                available: 20
            },
            {
                name: "Garderie du Soleil",
                distance: 7.5,
                price: 9,
                description: "Situé proche d'une école primaire et facilement accessible via l'autoroute 20, la Garderie du bonheur est la garderie parfaite pour les budgets moyens",
                available: 6
            }
        ];
    }
    
    public async query() {
        let result = await this.daycareService.getDayCares(this.distance, this.prix, this.nombreEnfants, this.location.lat, this.location.long);
        this.daycares = new Array();
        for (let daycare of result) {
            this.daycares.push(<DayCareViewModel>{
                name: daycare.name,
                description: daycare.description,
                available: daycare.available,
                distance: this.calculateDistance(this.location.lat, this.location.long, daycare.location.lat, daycare.location.lng)
            });
        }
    }
    
    private calculateDistance(lat1:number, long1:number, lat2:number, long2:number) : number {
        let p = 0.017453292519943295;    // Math.PI / 180
        let c = Math.cos;
        let a = 0.5 - c((lat1-lat2) * p) / 2 + c(lat2 * p) *c((lat1) * p) * (1 - c(((long1- long2) * p))) / 2;
        let dis = (12742 * Math.asin(Math.sqrt(a))); // 2 * R; R = 6371 km
        return dis;
    }
}
