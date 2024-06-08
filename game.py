from lib import TTTGame, TTTRandom


class TicTacToe:
    def __init__(self, p1, p2, random_iterations=0):
        self.p1 = p1
        self.p2 = p2
        self.game = TTTGame()
        randy = TTTRandom(iterations=random_iterations)
        randy.play(self.game)

    def play(self):
        self.__game_loop()
        print()
        print(self.__get_result())

    def __game_loop(self):
        while not self.game.is_over():
            self.game.display()
            print()
            
            move = None
            if self.game.player_turn == 1:
                move = self.p1.get_move(self.game)
            elif self.game.player_turn == 2:
                move = self.p2.get_move(self.game)

            status = self.game.move(move)
            if status == False:
                print('Wrong move try again!\n')

        self.game.display()

    def __get_result(self):
        winner = self.game.is_over()
        result = ''
        if winner == 3:
            result = 'Draw'
        elif winner == 0:
            result = 'Continue the game ...'
        else:
            result = f'Player {winner} won!'

        return result