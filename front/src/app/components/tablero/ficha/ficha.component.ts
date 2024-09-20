import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-ficha',
  standalone: true,
  imports: [],
  templateUrl: './ficha.component.html',
  styleUrl: './ficha.component.scss'
})
export class FichaComponent {
  @Input("value") value = "";
}
