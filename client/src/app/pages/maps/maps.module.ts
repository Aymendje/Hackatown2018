import { AgmCoreModule } from '@agm/core';
import { NgModule }       from '@angular/core';
import { CommonModule }   from '@angular/common';
import { FormsModule }    from '@angular/forms';
import { ThemeModule } from '../../@theme/theme.module';

import { GmapsComponent } from './gmaps.component';

@NgModule({
    imports: [
        ThemeModule,
        AgmCoreModule.forRoot({
            apiKey: 'AIzaSyCbMUwGg8XM6e9HXKTnjS1cY50Cgm9jDDM'
        }),
        CommonModule,
        FormsModule,
    ],
    declarations: [
        GmapsComponent
    ],
    providers: [
    ],
    exports: [
        GmapsComponent
    ]
})
export class MapsModule {}