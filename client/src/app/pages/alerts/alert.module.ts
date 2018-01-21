import { NgModule } from '@angular/core';

import { ThemeModule } from '../../@theme/theme.module';
import { CommonModule }   from '@angular/common';
import { MapsModule } from './../maps/maps.module';

import { AlertRoutingModule, routedComponents } from './alert-routing.module';
import { AlertService } from './alert.service';

@NgModule({
    imports: [
        CommonModule,
        ThemeModule,
        MapsModule,
        AlertRoutingModule
    ],
    exports: [],
    declarations: [
        ...routedComponents,
    ],
    providers: [
        AlertService
    ]
})
export class AlertModule { }