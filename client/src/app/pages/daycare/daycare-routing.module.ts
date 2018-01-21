import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DaycareComponent } from './daycare.component';
import { ReceiptComponent } from './receipts/receipt.component';

const routes: Routes = [
    {
        path: '',
        component: DaycareComponent
    },
    {
        path: 'receipts',
        component: ReceiptComponent
    },
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule],
})
export class DaycareRoutingModule { }

export const routedComponents = [
    DaycareComponent, 
    ReceiptComponent
];
