import { injectable, inject } from "inversify";
import { Router, Request, Response, NextFunction } from "express";
import Types from "./types";
import { Index } from "./routes/index";
import { Api } from "./routes/api";
@injectable()
export class Routes {

    public constructor(@inject(Types.Index) private index: Index,
                        @inject(Types.Api) private auth: Api) {}

    public get routes(): Router {
        const router: Router = Router();

        router.get("/",
                   (req: Request, res: Response, next: NextFunction) => this.index.helloWorld(req, res, next));
        router.post('/api/auth/register', (req: Request, res: Response, next: NextFunction) => this.auth.authRegister(req,res,next))
        router.post('/api/auth/login', (req: Request, res: Response, next: NextFunction) => this.auth.authLogin(req,res,next))

        router.get('/api/daycare', (req: Request, res: Response, next: NextFunction) => this.auth.getDayCare(req,res,next))
        
        return router;
    }
}
