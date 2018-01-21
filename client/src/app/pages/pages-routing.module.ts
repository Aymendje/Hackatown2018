import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [{
    path: '',
    component: PagesComponent,
    children: [
        {
            path: 'home',
            component: HomeComponent,
        },
        {
            path: 'daycare',
            loadChildren: './daycare/daycare.module#DaycareModule',
        },
        {
            path: 'sports',
            loadChildren: './sports/sports.module#SportsModule',
        },
        {
            path: 'alerts',
            loadChildren: './alerts/alert.module#AlertModule',
        },
        {
            path: '',
            redirectTo: 'home',
            pathMatch: 'full',
        },
    ],
}];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule],
})
export class PagesRoutingModule {
}
