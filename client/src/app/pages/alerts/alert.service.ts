import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions, URLSearchParams } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import { IAlert } from '../../../../../common/models/alert';
import { AlertViewModel } from './alert.viewmodel';
import { Definitions } from '../../../../../common/definitions';

@Injectable()
export class AlertService {

<<<<<<< HEAD
    private baseUrl = "http:/town.polypleb.com:3000/api/alerts";
=======
    private baseUrl = Definitions.ServerHostName + "/api/alerts";
>>>>>>> origin/master

    constructor(private http: Http) {

    }

    public getAlerts(distance: number,lat: number, long: number): Promise<IAlert[]> {

        let headers = new Headers({ 'Content-Type': 'application/json' });
        let params = new URLSearchParams();
        params.set('distance', distance.toString());
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

    public createAlerts(lat:number, long:number){
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let body = {
            lat : lat,
            long : long
        }
        let options = new RequestOptions(
            { 
                headers: headers,
                body: body
            }
        );
        this.http.post(this.baseUrl,body).toPromise().then((res)=>{
            return res.json();
        })
    }
}
