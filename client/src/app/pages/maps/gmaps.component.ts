import { Component, Input, Output, EventEmitter, SimpleChange } from '@angular/core';
import { OnInit, OnChanges } from '@angular/core/src/metadata/lifecycle_hooks';

@Component({
    selector: 'ngx-gmaps',
    styleUrls: ['./gmaps.component.scss'],
    template: `
    <nb-card>
        <nb-card-body>
            <agm-map [latitude]="lat" [longitude]="lng" [zoom]="13" (mapClick)="onClicked($event)">
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
    @Output() onClick = new EventEmitter<MouseEvent>();

    public ngOnInit() {
        console.log(this.markers);
    }

    public onClicked(event: MouseEvent) {
        this.onClick.emit(event);
    }

    public ngOnChanges(changes: {[propKey: string]: SimpleChange}) {
        // console.log(this.markers);
    }

    lat = 45.6307;
    lng = -72.9563;
}
