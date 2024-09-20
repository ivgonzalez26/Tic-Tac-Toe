import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { TableroComponent } from "./components/tablero/tablero.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, TableroComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'ticTacToe';
}
