import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { HttpClientModule } from "@angular/common/http";

import { AppComponent } from "./app.component";
import { MainComponent } from "./main-component/main.component";

import { BasicService } from "./basic.service";

@NgModule({
    declarations: [
        AppComponent,
        MainComponent
    ],
    imports: [
        BrowserModule,
        HttpClientModule
    ],
    providers: [
        BasicService
    ],
    bootstrap: [AppComponent]
})
export class AppModule { }
