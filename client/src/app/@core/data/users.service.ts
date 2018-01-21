import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { NbAuthSimpleToken, NbAuthService } from '@nebular/auth';
import { IUser } from "../../../../../common/IUser";
import 'rxjs/add/observable/of';
import { RequestOptions, Http, Headers } from '@angular/http';
import { Definitions } from '../../../../../common/definitions';

let counter = 0;

@Injectable()
export class UserService {

  private users = {
    nick: { name: 'Nick Jones', picture: 'assets/images/nick.png' },
    eva: { name: 'Eva Moor', picture: 'assets/images/eva.png' },
    jack: { name: 'Jack Williams', picture: 'assets/images/jack.png' },
    lee: { name: 'Lee Wong', picture: 'assets/images/lee.png' },
    alan: { name: 'Alan Thompson', picture: 'assets/images/alan.png' },
    kate: { name: 'Kate Martinez', picture: 'assets/images/kate.png' },
  };

  private userArray: any[];
  private currentUser: IUser;
  private currentUserChildren: any[];
  constructor(private authService: NbAuthService, private http: Http) {
    this.authService.onTokenChange().subscribe((token: NbAuthSimpleToken) => {
      if (token.getValue()){
        let obtainedVal = JSON.parse(token.getValue())
        console.log(obtainedVal)
        this.currentUser = obtainedVal as IUser;
        console.log(this.currentUser);
        this.getChildrenOfUser().then((childs) => {
          console.log(childs)
          this.currentUserChildren = childs;
        })
      } else {
        this.currentUser = null;
      }
    })
  }

  getChildrenOfUser(): Promise<any>{
    if (this.currentUser == null){
      return Promise.reject('Not authenticated');
    }
    let headers = new Headers({ 'Content-Type': 'application/json' });
    let params = new URLSearchParams();
    params.set('email', this.currentUser.emailAddress);

    let options = new RequestOptions(
        { 
            headers: headers,
            params: params
        }
    );

    return this.http.get(Definitions.ServerHostName+'/api/kids', options)
        .toPromise()
        .then((res) => {
            return res.json();
        });
    
  }

  setCurrentUser(u: any){
    this.currentUser =  u;
  }

  getUser(): Observable<IUser> {
    return Observable.of(this.currentUser);
  }
}
