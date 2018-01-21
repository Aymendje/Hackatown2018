import { Request, Response, NextFunction } from "express";
// import { Message } from "../../../common/communication/message";
import "reflect-metadata";
import { injectable, } from "inversify";
import { dayCare } from "../db";
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

        public getDayCare(req:Request, res :Response, next:NextFunction): void{
            
            let dist = req.params.distance;
            let price = req.params.price;
            let children = req.params.children;
            let center = req.params.center;
          
            dayCare.find(
                {
                    price :{
                        $lt : price
                    },
                    available :{
                        $gt : children
                    }
                }).
                then(
                    (dayCares:any[])=>{
                        let filteredData = dayCares.filter(
                            (v,i,a)=> {
                                return this.calculateDistance(v.location.lat,v.location.lng,center.lat,center.lng) <dist;  
                            }
                        )
                        res.json(filteredData);
                    }
                ).catch((reason)=>{
                    console.log(reason);
                    res.send(500);
                })
        }

        public getSpotEvents(req:Request, res:Response, next:NextFunction) : void{
            // let age =req.params.age;
            // let types = req.params.types;
            // let days = req.params.days;

            // dayCare.find

        }

        public getDayCareCamp(req:Request,res:Response, next:NextFunction) : void{
            
        }

        public getAlerts(req:Request, res:Response, next:NextFunction): void{

        }

        public createAlert(req:Request, res:Response, next:NextFunction) : void{

        }
       

        private calculateDistance(lat1:number,long1:number,lat2:number,long2:number) :number {
            let p = 0.017453292519943295;    // Math.PI / 180
            let c = Math.cos;
            let a = 0.5 - c((lat1-lat2) * p) / 2 + c(lat2 * p) *c((lat1) * p) * (1 - c(((long1- long2) * p))) / 2;
            let dis = (12742 * Math.asin(Math.sqrt(a))); // 2 * R; R = 6371 km
            return dis;
        }
    }
}

export = Route;
