import { IUser } from "../../common/IUser";
import { ILocation } from "../../common/ILocation";
import { IUserAuthInfo } from "./IUserAuthInfo";
export class User implements IUser{
    id: number;
    gender: boolean;
    givenName: string;
    surName: string;
    streetAddress: string;
    zipCode: string;
    emailAddress: string;
    userName: string;
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
    mass: number;
    height: number;
    location: ILocation;

    constructor() {
        // TODO
    }

    static fromDb(userInfo: IUserAuthInfo): User{
        // Fetch the db and return from info
        return new User()
    }
    
}