import { ILocation } from "./ILocation";

export interface IUser{
    // id: number;
    gender: boolean;
    givenName: string;
    surName: string;
    streetAddress: string;
    zipCode: string;
    emailAddress: string;
    userName: string;
    // To be defined where needed
    //Password: string;
    telephoneNumber: string;
    birthday: string;
    age: number;
    creditCardType: string;
    creditCardNumber: string;
    CVV2: number;
    creditCardExpirationDate: string;
    SSN: number;
    occupation: string;
    company: string;
    vehicle: string;
    bloodType: string;
    mass : number;
    height: number;
    location: ILocation
}