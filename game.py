from lib import TTTGame, TTTRandom, TTTHuman


class TicTacToe:
    def __init__(self, p1, p2, random_iterations=0):
        self.p1 = p1
        self.p2 = p2
        self.random_iterations = random_iterations
        self.game = TTTGame()
        self.random = TTTRandom()

    def play(self):
        self.__game_loop()
        print()
        print(self.__get_result())

    def __game_loop(self):
        while not self.game.is_over():
            self.game.display()
            print()
            
            player = None
            if self.game.player_turn == 1:
                player = self.p1
            elif self.game.player_turn == 2:
                player = self.p2

            if type(player) != TTTHuman and self.random_iterations != 0:
                self.random_iterations -= 1
                player = self.random

            move = player.get_move(self.game)
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
