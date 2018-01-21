import { NgModule } from '@angular/core';
import { AgmCoreModule } from '@agm/core';

import { ThemeModule } from '../../@theme/theme.module';

import { DaycareRoutingModule, routedComponents } from './daycare-routing.module';
import { DayCareService } from './daycare.service';

@NgModule({
  imports: [
    ThemeModule,
    AgmCoreModule.forRoot(),
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