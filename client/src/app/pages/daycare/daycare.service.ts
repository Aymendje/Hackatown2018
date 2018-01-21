import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions, URLSearchParams } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/toPromise';
import { IDayCare } from '../../../../../common/models/daycare';

@Injectable()
export class DayCareService {

    private baseUrl = "http:localhost:3000/api/daycare";

    constructor(private http: Http) {

    }

    public getDayCares(distance: number, price: number, childrenCount: number, lat: number, long: number): Promise<Array<IDayCare>> {

        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers });
        let url = `${this.baseUrl}?distance=${distance}&price=${price}&children=${childrenCount}&lat=${lat}&long=${long}`;

        return this.http.get(url, options)
            ._catch(this.handleError)
            .toPromise();
    }

    private handleError(error: Response) {
        console.error(error);
        return Observable.throw(error.json().error || "Server error");
    }
}
