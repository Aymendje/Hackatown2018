import { Component } from '@angular/core';

@Component({
    selector: 'ngx-gmaps',
    styleUrls: ['./gmaps.component.scss'],
    template: `
    <nb-card>
        <nb-card-body>
            <agm-map [latitude]="lat" [longitude]="lng">
                <agm-marker [latitude]="lat" [longitude]="lng"></agm-marker>
            </agm-map>
        </nb-card-body>
    </nb-card>
    `,
})
export class GmapsComponent {
    
    lat = 45.6307;
    lng = -72.9563;
}
