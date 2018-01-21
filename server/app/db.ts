import * as mongoose from "mongoose";
import { IDayCare } from './../../common/models/daycare';
import { ISportEvent } from './../../common/models/sportEvent';
import { IDayCareCamp } from './../../common/models/daycareCamp';
import { IAlert } from './../../common/models/alert';
import { IRegistration } from './../../common/models/eventRegister';


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
    tags : [String]
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
    eventType : String
});


export let dayCare = mongoose.model<IDayCareModel>("DayCare",dayCareSchema);
export let sportEvent = mongoose.model<ISportEventModel>("SportEvent",sportEventSchema);
export let dayCareCamp = mongoose.model<IDayCareCampModel>("DayCareCamp",dayCareCampSchema);
export let alert = mongoose.model<IAlertModel>("Alert", alertSchema);
export let registration = mongoose.model<IRegistrationModel>("Registration", registrationSchema);


(<any>mongoose.Promise) = global.Promise;
mongoose.connect("mongodb://Harambe:harambe@ds253587.mlab.com:53587/hackatown2018").catch((err) => {console.log(err)})
