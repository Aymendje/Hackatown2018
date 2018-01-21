export interface ISportEvent {
    _id: string;
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
    private : boolean;
    rating : number;
    photo : string;
    sport : string;
    days : string[];
};