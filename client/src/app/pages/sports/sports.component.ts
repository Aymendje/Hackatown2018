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
    public prix: number;
    public age: number;
    public text = "";

    public daycares: Array<any>;
    
    ngOnInit() {
        this.initialize();
    }
    
    private initialize() {
        this.distance = 5;
        this.age = 18;
        this.prix = 8;
    }
    
    public query() {
        // Calling the web service
        alert("query");
    }
}
