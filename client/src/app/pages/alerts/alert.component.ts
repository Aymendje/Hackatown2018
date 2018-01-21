import { Component, ChangeDetectionStrategy, ChangeDetectorRef } from '@angular/core';
import { OnInit } from '@angular/core/src/metadata/lifecycle_hooks';
import { IAlert } from './../../../../../common/models/alert';
import { AlertService } from './alert.service';
import { AlertViewModel } from './alert.viewmodel';
import { Observable } from 'rxjs/Observable';

@Component({
    selector: 'ngx-alert',
    templateUrl: './alert.component.html',
    styleUrls: ['./alert.css'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class AlertComponent implements OnInit {
    
    public distance: number;
    public alerts: AlertViewModel[];
    public canAddAlert : boolean;
    private location = {
        lat: 45.630692,
        long: -72.956329
    }

    private markers: Array<any>;

    public mapClick(event:MouseEvent){
        // console.log(event);
        if(this.canAddAlert)
            this.alertService.createAlerts((<any>event).coords.lat,(<any>event).coords.lng);
    }

    constructor(private alertService: AlertService, private cd: ChangeDetectorRef) {
       setInterval(() => { this.query(); }, 3000);
    }
    
    ngOnInit() {
        this.initialize();
    }
    
    private initialize() {
        this.distance = 50;
        this.query();
    }

    private toggleAlertCreate(){
        this.canAddAlert = !this.canAddAlert;
    }
    
    public select(daycare: AlertViewModel) {
        this.markers = [];
        this.markers.push({
            title: daycare.name,
            lat: daycare.location.lat,
            long: daycare.location.long
        });
        this.cd.markForCheck();
    }

    public query() {
        this.alertService.getAlerts(this.distance,this.location.lat, this.location.long).then((result) => {
            this.alerts = [];
            this.markers = [];
            for (let alert of result) {
                let x = {
                    name: alert.name,
                    description: "",
                    distance: this.calculateDistance(this.location.lat, this.location.long, alert.location.lat, alert.location.lng).toFixed(1),
                    location: {
                        lat: alert.location.lat,
                        long: alert.location.lng
                    }
                }
                this.alerts.push(x as AlertViewModel);
                this.markers.push( {
                    title: alert.name,
                    lat: alert.location.lat,
                    long: alert.location.lng
                });
            }
            this.alerts.sort((first, second) => {
                if (first.distance <= second.distance) {
                    return -1;
                }
                if (first.distance > second.distance) {
                    return 1;
                }
            })
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

    private 
}
