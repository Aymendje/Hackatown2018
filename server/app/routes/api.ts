import { Request, Response, NextFunction } from "express";
import "reflect-metadata";
import { injectable, } from "inversify";
import { dayCare,sportEvent,dayCareCamp,IDayCareCampModel,alert, registration } from "../db";

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

        public getDayCare(req:Request, res :Response, next:NextFunction): void{
            let dist = req.query['distance'];
            let price = req.query['price'];
            let children = req.query['children'];
            let lat = req.query['lat'];
            let long = req.query['long'];
            
            dayCare.find(
                {
                    price :{
                        $lte : price
                    },
                    available :{
                        $gte : children
                    }
                }).
                then(
                    (dayCares:any[])=>{
                        let filteredData = dayCares.filter(
                            (v,i,a)=> {
                                let calDistance = this.calculateDistance(v.location.lat,v.location.lng, lat, long);
                                return  calDistance < dist;  
                            }
                        )
                        
                        res.json(filteredData);
                    }
                ).catch((reason: any)=>{
                    console.log(reason);
                    res.send(500);
                })
        }

        public getSpotEvents(req:Request, res:Response, next:NextFunction) : void{
           
            // Test data
            // let age = 15;
            // let types = ["Patin", "Ete","Soccer"];
            // let days = ["Mardi","Jeudi"];
            console.log(req.query)
            let age = req.query['age'];
            let types = req.query['types'];
            types = JSON.parse(types);
            let days = req.query['days'];
            days = JSON.parse(days)
            let lat = req.query['lat'];
            let long = req.query['long'];
            let dist = req.query['distance'];
            console.log(days)
            console.log(types)
            sportEvent.find({
                // Find events based on age
                minAge: {
                    $lte: age
                },
            }).then(
                (sportEvents:any[])=>{
                    let filteredData = sportEvents.filter((v,i,a) =>
                    {
                        // Check for tags intesection
                        return this.intersect(types,v.tags).length > 0 &&
                        // Check for date intersection 
                               this.intersect(days,v.days).length > 0 &&
                               this.calculateDistance(v.location.lat,v.location.lng, lat, long) <dist;
                    });
                    res.json(filteredData);
                }
            ).catch((reason)=>{
                console.log(reason);
                res.send(500);
            })

        }

        public getDayCareCamp(req:Request,res:Response, next:NextFunction) : void{
            // Test data
        //    let testminAge = 5;
        //    let testmaxAge = 10;
        //    let types = ["Science", "Art"];
        //    let startDate = new Date(2018,4,5);
        //    let endDate = new Date(2018,8,18);

        let testminAge = req.params.minAge;
        let testmaxAge = req.params.maxAge;
        let types = req.params.tags;
        let startDate = req.params.startDate;
        let endDate =req.params.endDate;
        let lat = req.params.lat;
        let long = req.params.long;
        let dist = req.params.distance;

            dayCareCamp.find({
                minAge:{
                    $lte: testminAge
                },
                maxAge :{
                    $gte:testmaxAge
                }
            }).then(
                (dayCareCamps:IDayCareCampModel[])=>{
                    let filteredData = dayCareCamps.filter((v,i,a)=>
                    {
                        let validStartDate = v.startDate < startDate;
                        let validEndDate = v.endDate > endDate;
                        return this.intersect(types,v.tags).length > 0
                        &&
                        validStartDate
                        &&
                        validEndDate
                        &&
                        this.calculateDistance(v.location.lat,v.location.lng, lat, long) <dist;
                    });
                res.json(filteredData);     
            }).catch((reason)=>{
                console.log(reason);
                res.send(500);
            })
        }

        public getAlerts(req:Request, res:Response, next:NextFunction): void{
          
            let dist = 20;
            let lat = 45.5801883;
            let long = -73.1624795;
            let types = ["Fire","Yonni"];

            // let dist = req.params.distance;
            // let lat = req.params.lat;
            // let long = req.params.long;
            // let types = req.params.types;
            alert.find({ }).then((alerts:any[])=>{
                let filteredData = alerts.filter((v,i,a)=>{
                    let calculatedDistance = this.calculateDistance(v.location.lat,v.location.lng, lat, long);
                    let hasTypeIntersect = this.intersect(types,v.tags).length > 0;
                    return calculatedDistance < dist && hasTypeIntersect;
                });
                res.json(filteredData);     
            });
    
        }

        public createAlert(req:Request, res:Response, next:NextFunction) : void{
            
            // let name = "Fire Alert";
            // let lat = 45.5801883 + Math.random()/3;
            // let long =  -73.1624795  + Math.random()/3;
            // let types = ["Fire"];
            // let description = "SHITS ON FIRE YO!";

            let name = req.body.name;
            let types = req.body.types;
            let description = req.body.description;
            let lat = req.body.lat;
            let long = req.body.long;


            let newAlert = new alert();
            newAlert.name = name;
            newAlert.description = description;
            newAlert.location.lat = lat;
            newAlert.location.lng = long;
            newAlert.tags = types;
            newAlert.save();
            res.send(201);  
        }


        public createRegistration(req: Request, res:Response, next:NextFunction):void {
            let kidId = req.body.kidId;
            let eventId = req.body.eventId;
            let eventType = req.body.eventType;

            let newRegistration = new registration();
            newRegistration.kidId = kidId;
            newRegistration.eventId = eventId;
            newRegistration.eventType = eventType;

            newRegistration.save();
            res.send(201);
        }
       
        public getRegistration(req: Request, res:Response, next:NextFunction):void{
            let kidId = req.params.kidId;
            let eventId = req.params.eventId;
            let eventType = req.params.eventType;

            registration.find({
                kidId : kidId,
                eventId : eventId,
                eventType : eventType
            }).then(
                (registrations:any[])=>{
                    res.send(registrations)
                }).catch((reason)=>{
                    console.log(reason);
                    res.send(500);
                })
        }

        public getAllRegistrations(req:Request, res:Response, next:NextFunction):void{
            let kidId = req.params.kidId;

            registration.find({
                kidId:kidId
            }).then((registrations:any[])=>{
                res.send(registrations);
            }).catch((reason)=>{
                console.log(reason);
                res.send(500);
            })
        }

        private calculateDistance(lat1:number,long1:number,lat2:number,long2:number) :number {
            let p = 0.017453292519943295;    // Math.PI / 180
            let c = Math.cos;
            let a = 0.5 - c((lat1-lat2) * p) / 2 + c(lat2 * p) *c((lat1) * p) * (1 - c(((long1- long2) * p))) / 2;
            let dis = (12742 * Math.asin(Math.sqrt(a))); // 2 * R; R = 6371 km
            return dis;
        }

        private intersect(a:string[], b:string[]):string[] {
            var t;
            if (b.length > a.length) t = b, b = a, a = t; // indexOf to loop over shorter
            return a.filter((e:string)=> {
                return b.indexOf(e) > -1;
            });
        }
    }
}

export = Route;
