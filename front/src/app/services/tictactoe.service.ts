import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TictactoeService {

  constructor(private http: HttpClient) { }

  get_board(): Promise<any> {
    return this.http.get("http://localhost:8888/board").toPromise();
  }

  player_move(row: Number, col: Number): Promise<any> {
    let data: any = {
      row: row,
      col: col
    }
    return this.http.post("http://localhost:8888/board", JSON.stringify(data)).toPromise();
  }

  check_winner(): Promise<any> {
    return this.http.get("http://localhost:8888/check_winner").toPromise();
  }

  move_pc(): Promise<any> {
    return this.http.get("http://localhost:8888/move_pc").toPromise();
  }

}
