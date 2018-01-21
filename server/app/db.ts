import * as mongoose from "mongoose";
import { IDayCare } from './../../common/models/daycare';
import { ISportEvent } from './../../common/models/sportEvent';
import { IDayCareCamp } from './../../common/models/daycareCamp';
import { IChild } from './../../common/models/child';
import { IAlert } from './../../common/models/alert';
import { IRegistration } from './../../common/models/eventRegister';
import { IUser } from "../../common/IUser";


export interface IDayCareModel extends IDayCare, mongoose.Document{}
let dayCareSchema = new mongoose.Schema({
    name: String,
    description: String,
    address: String,
    tel : String,
    location :{
        lng : Number,
        lat: Number
    },
    price : Number,
    rating : Number,
    photo : String,
    available : Number,
    private : Boolean
});

export interface ISportEventModel extends ISportEvent, mongoose.Document{}
let sportEventSchema = new mongoose.Schema({
    name: String,
	description: String,
    address: String,
    tel : String,
    location :{
        lng : Number,
        lat: Number
    },
    price : Number,
    available: Number,
    minAge : Number,
    days : [String],
    sport : String
});


export interface IDayCareCampModel extends IDayCareCamp, mongoose.Document{}
let dayCareCampSchema = new mongoose.Schema({
    name: String,
	description: String,
    address: String,
    tel : String,
    location :{
        lng : Number,
        lat: Number
    },
    price : Number,
    available: Number,
    minAge : Number,
    maxAge : Number,
    startDate : Date,
    endDate : Date,
    tags : [String],
});


export interface IAlertModel extends IAlert, mongoose.Document{}
let alertSchema = new mongoose.Schema({
    name: String,
	description: String,
    location :{
        lng : Number,
        lat: Number
    },
    photo : String,
    tags : [String]
});

export interface IRegistrationModel extends IRegistration, mongoose.Document{}
let registrationSchema = new mongoose.Schema({
    kidId: String,
    eventId : String,
    eventType : String,
    cost : Number
});

export interface IServerUser extends IUser, mongoose.Document{}
let serverUserSchema = new mongoose.Schema({
    // id: Number,
    gender: Boolean,
    givenName: String,
    surName: String,
    streetAddress: String,
    zipCode: String,
    emailAddress: String,
    userName: String,
    // This user has the password in server side
    password: String,
    telephoneNumber: String,
    birthday: String,
    age: Number,
    creditCardType: String,
    creditCardNumber: Number,
    CVV2: Number,
    creditCardExpirationDate: String,
    SSN: Number,
    occupation: String,
    company: String,
    vehicle: String,
    bloodType: String,
    mass: Number,
    height: Number,
    location:{
        lat: Number,
        lng : Number
    },
    children: [Number]
})

export interface IChildModel extends IChild, mongoose.Document{}
let childchema = new mongoose.Schema({
    oid: String,
    gender: Boolean,
    givenName: String,
    surName: String,
    birthday: String,
    age: Number,
    bloodType: String,
    mass: Number,
    height: Number,
    parents: [Number],
})
export let child = mongoose.model<IChildModel>("Child", childchema)
export let user = mongoose.model<IServerUser>("Peoples", serverUserSchema);
export let dayCare = mongoose.model<IDayCareModel>("DayCare",dayCareSchema);
export let sportEvent = mongoose.model<ISportEventModel>("SportEvent",sportEventSchema);
export let dayCareCamp = mongoose.model<IDayCareCampModel>("DayCareCamp",dayCareCampSchema);
export let alert = mongoose.model<IAlertModel>("Alert", alertSchema);
export let registration = mongoose.model<IRegistrationModel>("Registration", registrationSchema);


(<any>mongoose.Promise) = global.Promise;
mongoose.connect("mongodb://Harambe:harambe@ds253587.mlab.com:53587/hackatown2018").catch((err) => {console.log(err)})
