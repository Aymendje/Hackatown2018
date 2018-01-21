export interface IDayCareCamp {
	name: string;
	description: string;
    address: string;
    tel : string;
    location :{
        lng : number;
        lat: number;
    }
    price : number;
    rating : number;
    photo : string;
    available: number;
    tags : string[];
    startDate : Date;
    endDate : Date;
    ageMin: number;
    ageMax : number;
};