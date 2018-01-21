import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions, URLSearchParams } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import { ISportEvent } from '../../../../../common/models/sportEvent';
import { SportViewModel } from './sports.viewmodel';
import { Definitions } from '../../../../../common/definitions';

@Injectable()
export class SportsService {

<<<<<<< HEAD
    private baseUrl = "http:/town.polypleb.com:30000/api/sportEvent";
=======
    private baseUrl = Definitions.ServerHostName+'/api/sportEvent';
>>>>>>> origin/master

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

        this.http.post(Definitions.ServerHostName+ '/api/registration', body).toPromise().then((res)=>{
            return res.json();
        });
    }
}
