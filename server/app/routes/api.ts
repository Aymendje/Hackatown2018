import { Request, Response, NextFunction } from "express";
import { Message } from "../../../common/communication/message";
import "reflect-metadata";
import { injectable, } from "inversify";

module Route {
    const AcceptedUsers: IUserAuthInfo[] = [
        {
            email: 'polyball@bidon.com',
            password: 'qwerty123',
            otherInformation: 'Je suis un chevreuil'
        }
    ]

    export interface IUserAuthInfo{
        email: string;
        password: string;
        otherInformation: string;
    }

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
                res.json({
                    'token': 'abcde'
                })
            } else {
                res.sendStatus(403);
            }
        }
    }
}

export = Route;
