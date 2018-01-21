import { NgModule } from '@angular/core';
import { ThemeModule } from '../../@theme/theme.module';

import { CommonModule }   from '@angular/common';
import { MapsModule } from './../maps/maps.module';

import { SportsRoutingModule, routedComponents } from './sports-routing.module';
import { SportsService } from './sports.service';

@NgModule({
    imports: [
        CommonModule,
        ThemeModule,
        MapsModule,
        SportsRoutingModule
    ],
    exports: [],
    declarations: [
        ...routedComponents,
    ],
    providers: [
        SportsService
    ]
})
export class SportsModule { }