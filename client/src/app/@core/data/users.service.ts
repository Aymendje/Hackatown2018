import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { NbAuthSimpleToken, NbAuthService } from '@nebular/auth';
import { IUser } from "../../../../../common/IUser";
import 'rxjs/add/observable/of';

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
  constructor(private authService: NbAuthService) {
    this.authService.onTokenChange().subscribe((token: NbAuthSimpleToken) => {
      if (token.getValue()){
        let obtainedVal = JSON.parse(token.getValue())
        console.log(obtainedVal)
        this.currentUser = obtainedVal as IUser;
        console.log(this.currentUser);
      }
    })
  }

  setCurrentUser(u: any){
    this.currentUser =  u;
  }

  getUser(): Observable<IUser> {
    return Observable.of(this.currentUser);
  }
}
