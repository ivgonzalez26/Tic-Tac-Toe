import tornado.ioloop
import tornado.web
import json
from game import TicTacToe

tictactoe = TicTacToe()

class TicTacToeHandler(tornado.web.RequestHandler):
    def initialize(self, game):
        self.game = game

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

    def options(self):
        self.set_status(204)
        self.finish()

    def get(self):
        self.write(self.game.get_board())

    def post(self):
        try:
            data = json.loads(self.request.body)
            row = data.get("row")
            col = data.get("col")

            if row is None or col is None:
                raise ValueError("Se requiere 'row' y 'col'")

            if not self.game.player_move(row, col):
                self.set_status(400)
                self.write({"error": "Movimiento inválido"})
            else:
                self.write(self.game.get_board())
        
        except Exception as e:
            self.set_status(400)
            self.write({"error": str(e)})

class TicTacToePCMoveHandler(tornado.web.RequestHandler):
    def initialize(self, game):
        self.game = game

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

    def options(self):
        self.set_status(204)
        self.finish()

    def get(self):
        self.game.pc_move()
        self.write(self.game.get_board())

    
class CheckWinnerHandler(tornado.web.RequestHandler):
    def initialize(self, game):
        self.game = game

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

    def options(self):
        self.set_status(204)
        self.finish()

    def get(self):
        self.game.pc_move()
        self.write(self.game.check_winner())

def make_app():
    return tornado.web.Application([
        (r"/board", TicTacToeHandler, dict(game=tictactoe)),      
        (r"/move_pc", TicTacToePCMoveHandler, dict(game=tictactoe)),
        (r"/check_winner", CheckWinnerHandler, dict(game=tictactoe)),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888) 
    print("Servidor escuchando en http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
