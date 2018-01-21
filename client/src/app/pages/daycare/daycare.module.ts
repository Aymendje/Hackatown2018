import { NgModule } from '@angular/core';

import { ThemeModule } from '../../@theme/theme.module';
import { CommonModule }   from '@angular/common';
import { MapsModule } from './../maps/maps.module';

import { DaycareRoutingModule, routedComponents } from './daycare-routing.module';
import { DayCareService } from './daycare.service';

@NgModule({
    imports: [
        CommonModule,
        ThemeModule,
        MapsModule,
        DaycareRoutingModule
    ],
    exports: [],
    declarations: [
        ...routedComponents,
    ],
    providers: [
        DayCareService
    ]
})
export class DaycareModule { }