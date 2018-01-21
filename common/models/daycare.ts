export interface IDayCare {
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
    rating : number;
    photo : string;
    available: number;
    private : boolean;
};