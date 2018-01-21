import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions, URLSearchParams } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import { IDayCare } from '../../../../../common/models/daycare';
import { DayCareViewModel } from './daycare.viewmodel';

@Injectable()
export class DayCareService {

    private baseUrl = "http://localhost:3000/api/daycare";

    constructor(private http: Http) {

    }

    public getDayCares(distance: number, price: number, childrenCount: number, lat: number, long: number): Promise<IDayCare[]> {

        let headers = new Headers({ 'Content-Type': 'application/json' });
        let params = new URLSearchParams();
        params.set('distance', distance.toString());
        params.set('price', price.toString());
        params.set('children', childrenCount.toString());
        params.set('lat', lat.toString());
        params.set('long', long.toString());

        let options = new RequestOptions(
            { 
                headers: headers,
                params: params
            }
        );

        return this.http.get(this.baseUrl, options)
            .toPromise()
            .then((res) => {
                return res.json();
            });
    }
}
