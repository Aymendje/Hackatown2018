import { NgModule } from '@angular/core';
import { ThemeModule } from '../../@theme/theme.module';

import { CommonModule }   from '@angular/common';
import { MapsModule } from './../maps/maps.module';

import { SportsRoutingModule, routedComponents } from './sports-routing.module';

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
})
export class SportsModule { }