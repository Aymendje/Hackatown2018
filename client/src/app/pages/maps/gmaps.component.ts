import { Component, Input, SimpleChange } from '@angular/core';
import { OnInit, OnChanges } from '@angular/core/src/metadata/lifecycle_hooks';

@Component({
    selector: 'ngx-gmaps',
    styleUrls: ['./gmaps.component.scss'],
    template: `
    <nb-card>
        <nb-card-body>
            <agm-map [latitude]="lat" [longitude]="lng" [zoom]="13">
                <agm-marker *ngFor="let marker of markers" [latitude]="marker.lat" [longitude]="marker.long">
                    <agm-info-window>{{marker.title}}</agm-info-window>
                </agm-marker>
            </agm-map>
        </nb-card-body>
    </nb-card>
    `,
})
export class GmapsComponent implements OnInit, OnChanges {
    
    @Input()
    public markers;

    private lat = 45.6307;
    private lng = -72.9563;

    public ngOnInit() {
    }

    public ngOnChanges(changes: {[propKey: string]: SimpleChange}) {
    }
}
