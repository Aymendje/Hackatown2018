import * as mongoose from "mongoose";
import { IDayCare } from './../../common/models/daycare';

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

export let dayCare = mongoose.model<IDayCareModel>("DayCare",dayCareSchema);
(<any>mongoose.Promise) = global.Promise;
mongoose.connect("mongodb://Harambe:harambe@ds253587.mlab.com:53587/hackatown2018").catch((err) => {console.log(err)})