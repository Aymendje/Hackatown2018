import { IUser } from "../../common/IUser";
import { ILocation } from "../../common/ILocation";
import { IUserAuthInfo } from "./IUserAuthInfo";
export class User implements IUser{

    constructor() {
        // TODO
    }

    static fromDb(userInfo: IUserAuthInfo): User{
        // Fetch the db and return from info
        return new User()
    }
    Id: number;
    Gender: boolean;
    GivenName: string;
    SurName: string;
    StreetAddress: string;
    ZipCode: string;
    EmailAddress: string;
    UserName: string;
    // This user has the password in server side
    Password: string;
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
    Mass: number;
    Height: number;
    Location: ILocation;
}