import * as mongoose from "mongoose";
import { IDayCare } from './../../common/models/daycare';
import { ISportEvent } from './../../common/models/sportEvent';


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

export let dayCare = mongoose.model<IDayCareModel>("DayCare",dayCareSchema);
export let sportEvent = mongoose.model<ISportEventModel>("SportEvent",sportEventSchema);
(<any>mongoose.Promise) = global.Promise;
mongoose.connect("mongodb://Harambe:harambe@ds253587.mlab.com:53587/hackatown2018").catch((err) => {console.log(err)})