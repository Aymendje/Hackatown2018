import { ILocation } from "./ILocation";

export interface IUser{
    Id: number;
    Gender: boolean;
    GivenName: string;
    SurName: string;
    StreetAddress: string;
    ZipCode: string;
    EmailAddress: string;
    UserName: string;
    // To be defined where needed
    //Password: string;
    TelephoneNumber: string;
    Birthday: string;
    Age: number;
    CreditCardType: string;
    CreditCardNumber: string;
    CVV2: number;
    CreditCardExpirationDate: string;
    SSN: number;
    Occupation: string;
    Company: string;
    Vehicle: string;
    BloodType: string;
    Mass : number;
    Height: number;
    Location: ILocation
}