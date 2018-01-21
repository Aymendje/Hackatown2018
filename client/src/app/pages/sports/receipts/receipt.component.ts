import { Component, Input, SimpleChange } from '@angular/core';
import { OnInit, OnChanges } from '@angular/core/src/metadata/lifecycle_hooks';

@Component({
    selector: 'ngx-receipt',
    styleUrls: ['./receipt.css'],
    templateUrl: './receipt.component.html',
})
export class ReceiptComponent implements OnInit, OnChanges {

    private receipts = [
        {
            title: "Frais de garderie",
            date: "20/10/2013",
            price: 195,
            isPaid: true,
        },
        {
            title: "Service alimentaire",
            date: "26/10/2013",
            price: 75,
            isPaid: false,
        }
    ]

    public ngOnInit() {
    }

    public ngOnChanges(changes: {[propKey: string]: SimpleChange}) {
    }
}
