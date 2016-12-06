class Player:
    def __init__(self, marker, name):
        self.marker = marker
        self.name = name

class TicTacToe:
    def __init__(self):
        self.player1 = Player('X', 'Player 1')
        self.player2 = Player('O', 'Player 2')
        self.record = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.record_to_board();
        self.moves = 0
        self.current = self.player1;
        print('Welcome to TicTacToe!')
        self.prompt()
        
    def record_to_board(self):
        self.convert = []
        for i in range(0, 7, 3):
            line = self.record[i:i+3]
            index = i//3
            self.convert.append(" ".join(line))
          
        self.board = "\n".join(self.convert)

    def play(self, position):
      
        if self.record[position] == 'X' or self.record[position] == 'O':
            print('Invalid move! Pick an open space!')
            return self.prompt()
        elif position < 0 or position > 8:
            print('Invalid input! Pick an open space!')
            return self.prompt()
        else:
            self.record[position] = self.current.marker
            self.moves = self.moves + 1
            
            if self.win():
                self.record_to_board()
                print(self.board)
                return
            elif self.current.name == self.player1.name:
                self.current = self.player2
            else:
                self.current = self.player1
        
        if self.moves < 9:
            self.record_to_board()
            self.prompt()
          
        else:
            print('Game over! It is a draw!')
          
          
    def prompt(self):
      
        print(self.board)
        move = input(self.current.name + ' it is your move. Pick a position to mark on the board.\n')

        try: 
            move = int(move) - 1

        except ValueError:
            print ('Invalid move! Pick an open space!')
            return self.prompt()

        self.play(move)
        
    def win(self):
        
        gameOver = False
        
        if self.record[0] == self.record[1] and self.record[1] == self.record[2]:
            print('Game over! ' + self.current.name + ' wins!')
            gameOver = True
          
        elif self.record[3] == self.record[4] and self.record[4] == self.record[5]:
            print('Game over! ' + self.current.name + ' wins!')
            gameOver = True
        
        elif self.record[6] == self.record[7] and self.record[7] == self.record[8]:
            print('Game over! ' + self.current.name + ' wins!')
            gameOver = True
          
        elif self.record[0] == self.record[3] and self.record[3] == self.record[6]:
            print('Game over! ' + self.current.name + ' wins!')
            gameOver = True
          
        elif self.record[1] == self.record[4] and self.record[4] == self.record[7]:
            print('Game over! ' + self.current.name + ' wins!')
            gameOver = True

        elif self.record[2] == self.record[5] and self.record[5] == self.record[8]:
            print('Game over! ' + self.current.name + ' wins!')
            gameOver = True

        elif self.record[0] == self.record[4] and self.record[4] == self.record[8]:
            print('Game over! ' + self.current.name + ' wins!')
            gameOver = True
          
        elif self.record[2] == self.record[4] and self.record[4] == self.record[6]:
            print('Game over! ' + self.current.name + ' wins!')
            gameOver = True

        return gameOver 

TicTacToe()