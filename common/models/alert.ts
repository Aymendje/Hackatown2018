export interface IAlert {
    name: string;
    description : string;
    location :{
        lng : number;
        lat: number;
    }
    photo : string;
    tags : string[];
};