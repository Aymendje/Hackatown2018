import { AfterViewInit, Component, HostListener } from "@angular/core";

@Component({
    moduleId: module.id,
    selector: "main-component",
    templateUrl: "./main.component.html",
    styleUrls: ["./main.component.css"]
})

export class MainComponent implements AfterViewInit {

    // @ViewChild("container")
    // private containerRef: ElementRef;

    public constructor() { }

    @HostListener("window:resize", ["$event"])
    public onResize(): void {
        // this.renderService.onResize();
    }

    @HostListener("window:keydown", ["$event"])
    public onKeyDown(event: KeyboardEvent): void {
        // this.renderService.handleKeyDown(event);
    }

    @HostListener("window:keyup", ["$event"])
    public onKeyUp(event: KeyboardEvent): void {
        // this.renderService.handleKeyUp(event);
    }

    public ngAfterViewInit(): void {
        // this.renderService
        //     .initialize(this.containerRef.nativeElement)
        //     .then(/* do nothing */)
        //     .catch((err) => console.error(err));
    }
}
