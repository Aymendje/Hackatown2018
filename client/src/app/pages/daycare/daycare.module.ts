import { NgModule } from '@angular/core';
import { AgmCoreModule } from '@agm/core';

import { ThemeModule } from '../../@theme/theme.module';

import { DaycareRoutingModule, routedComponents } from './daycare-routing.module';

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
})
export class DaycareModule { }