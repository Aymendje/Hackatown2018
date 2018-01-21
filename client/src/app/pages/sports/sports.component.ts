import { Component, ChangeDetectionStrategy } from '@angular/core';
import { OnInit } from '@angular/core/src/metadata/lifecycle_hooks';
import { SportsService } from './sports.service';
import { ISportEvent } from '../../../../../common/models/sportEvent';
import { SportViewModel } from "./sports.viewmodel";

@Component({
    selector: 'ngx-sports',
    templateUrl: './sports.component.html',
    styleUrls: ['./sports.css'],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SportsComponent implements OnInit {
    
    public distance: number;
    public prix: number;
    public ageMaximal: number;
    public text = "";
    private location = {
        lat: 45.630692,
        long: -72.956329
    }

    public nombreEnfants: number;
    public sportEvents: Array<SportViewModel>;
    public lundiChecked: boolean;
    public mardiChecked: boolean;
    public mercrediChecked: boolean;
    public jeudiChecked: boolean;
    public vendrediChecked: boolean;
    public finDeSemaineChecked: boolean;
    
    public badmintonChecked: boolean;
    public hockeyChecked: boolean;
    public natationChecked: boolean;
    public basketballChecked: boolean;
    public soccerChecked: boolean;
    public karateChecked: boolean;
    
    constructor(private sportsService: SportsService) {
        
    }

    ngOnInit() {
        this.initialize();
    }
    
    private initialize() {
        this.distance = 5;
        this.ageMaximal = 18;
        this.prix = 8;
        this.nombreEnfants = 1;
        // Days
        this.lundiChecked = false;
        this.mardiChecked = false;
        this.mercrediChecked = false;
        this.jeudiChecked = false;
        this.vendrediChecked = false;
        this.finDeSemaineChecked = false;
        // Types
        this.badmintonChecked = false;
        this.hockeyChecked = false;
        this.natationChecked = false;
        this.basketballChecked = false;
        this.soccerChecked = false;
        this.karateChecked = false;
    }
    
    public getDays(): string[] {
        let days = [];
        if (this.lundiChecked)
            days.push("lundi")
        if (this.mardiChecked)
            days.push("mardi")
        if (this.mercrediChecked)
            days.push("mercredi")
        if (this.jeudiChecked)
            days.push("jeudi")
        if (this.vendrediChecked)
            days.push("vendredi")
        if (this.finDeSemaineChecked)
            days.push("finDeSemaine")
        return days;
    }

    public getTypes(): string[]{
        let types = [];
        if (this.badmintonChecked)
            types.push("badminton")
        if (this.hockeyChecked)
            types.push("hockey")
        if (this.natationChecked)
            types.push("natation")
        if (this.basketballChecked)
            types.push("basketball")
        if (this.soccerChecked)
            types.push("soccer")
        if (this.karateChecked)
            types.push("karate")
        return types;
    }

    public query() {
        let daysChecked = this.getDays();
        console.log(daysChecked)
        let typesChecked = this.getTypes();
        console.log(typesChecked)        
        this.sportsService.getSportEvents(this.distance, this.location.lat, this.location.long, daysChecked, typesChecked, this.ageMaximal).then((v: ISportEvent[])=>{
            console.log(`Something`)
            v.forEach((element) => {
                let x = {
                    age: 42,
                    days: element.days,
                    lat: element.location.lng,
                    long: element.location.lng,
                    distance: this.calculateDistance(this.location.lat, this.location.long, element.location.lat, element.location.lng).toFixed(1),
                    types: element.tags
                }
                this.sportEvents.push(x);
            })
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
