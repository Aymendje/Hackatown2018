import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions, URLSearchParams } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import { ISportEvent } from '../../../../../common/models/sportEvent';
import { SportViewModel } from './sports.viewmodel';

@Injectable()
export class SportsService {

    private baseUrl = "http://localhost:3000/api/sportEvent";

    constructor(private http: Http) {

    }

    public getSportEvents(distance: number, lat: number, long: number, days: string[], types: string[], ageMaximum: number): Promise<ISportEvent[]> {

        let headers = new Headers({ 'Content-Type': 'application/json' });
        let params = new URLSearchParams();
        params.set('distance', distance.toString());
        params.set('age', ageMaximum.toString());
        params.set('days', JSON.stringify(days));
        params.set('types', JSON.stringify(types));
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

    public registerKid(sportEvent: SportViewModel) {
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let body = {
            kidId : sportEvent.kid,
            eventId : sportEvent.id,
            eventType: "sports"
        }
        let options = new RequestOptions(
            { 
                headers: headers,
                body: body
            }
        );
        this.http.post(`http://localhost:3000/api/registration`, body).toPromise().then((res)=>{
            return res.json();
        });
    }
}
