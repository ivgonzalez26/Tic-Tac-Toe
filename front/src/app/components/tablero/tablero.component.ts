import { Component, OnInit } from '@angular/core';
import { FichaComponent } from "./ficha/ficha.component";
import { TictactoeService } from '../../services/tictactoe.service';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-tablero',
  standalone: true,
  imports: [FichaComponent, HttpClientModule],
  providers: [TictactoeService],
  templateUrl: './tablero.component.html',
  styleUrl: './tablero.component.scss'
})
export class TableroComponent implements OnInit {
  tablero = [["", "", ""],
              ["", "", ""],
              ["", "", ""]];
  
  constructor(private tictactoeService: TictactoeService) {}

  ngOnInit(): void {
    
  }
  
  player_move(row: Number, col: Number) {
    this.tictactoeService.player_move(row,col).then( r => {
      this.tictactoeService.move_pc().then( r => {
        this.tictactoeService.get_board().then( r => {
          this.tablero = r;
          this.tictactoeService.check_winner()
        }).catch(e => console.log(e));
      }).catch( e => console.log(e));
    }).catch( e => console.log(e) );  
  }
}
