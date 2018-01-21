import { Request, Response, NextFunction } from "express";
import "reflect-metadata";
import { injectable, } from "inversify";
import { IUserAuthInfo } from "../IUserAuthInfo";
import { User } from "../User";

module Route {
    const AcceptedUsers: IUserAuthInfo[] = [
        {
            email: 'polyball@bidon.com',
            password: 'qwerty123',
            otherInformation: 'Je suis un chevreuil'
        }
    ]

    

    @injectable()
    export class Api {

        public authRegister(req: Request, res: Response, next: NextFunction): void {
            res.sendStatus(200);
        }

        public authLogin(req: Request, res: Response, next: NextFunction): void {
            console.log(req.body)
            let email = req.body.email;
            let pwd = req.body.password;
            let userFound = AcceptedUsers.find((element) => {
                return element.email === email && element.password === pwd;
            })
            console.log(userFound)
            if (userFound){
                let theUser = new User();
                theUser.Gender = true;
                theUser.Age = 42;
                theUser.UserName = 'Yonni'
                res.json({
                    'data': {
                        'token': JSON.stringify(theUser)
                    }
                })
            } else {
                res.sendStatus(403);
            }
        }
    }
}

export = Route;
