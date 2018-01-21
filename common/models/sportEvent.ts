export interface ISportEvent {
	name: string;
	description: string;
    address: string;
    tel : string;
    location :{
        lng : number;
        lat: number;
    }
    price : number;
    available: number;
    minAge : number;
    days : string[];
    tags : string[];
};