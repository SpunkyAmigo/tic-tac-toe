from lib import TTTGame, TTTHuman, TTTRandom, TTTConfidentAI, TTTHopelessAI, clear_console
import time

game = TTTGame()

randy = TTTRandom(iterations=1)

ai1 = TTTConfidentAI(1, 12)
ai2 = TTTConfidentAI(2, 12)

hopeless1 = TTTHopelessAI(1, 12)
hopeless2 = TTTHopelessAI(2, 12)

human = TTTHuman()

# randy.play(game)

# Def gonna loose
# game.move((0, 0))
# game.move((0, 2))
# game.move((2, 0))

# Def gonna loose in many ways
# game.move((1, 1))
# game.move((1, 2))
# game.move((2, 2))


# game.move((1, 0))
# game.move((1, 2))

# Making a fool
# game.move((1, 1))
# game.move((0, 1))
# game.move((1, 0))
# game.move((0, 2))

# clear_console()

iteration = 0

while not game.is_over():
    iteration += 1
    # clear_console()
    
    game.display()
    print()
    
    move = None
    if game.player_turn == 1:
        move = ai1.get_move(game)
    elif game.player_turn == 2:
        move = ai2.get_move(game)

    status = game.move(move)
    if status == False:
        print('Wrong move try again!')

    print()
    
# clear_console()

game.display()

print()
print()

winner = game.is_over()
if winner == 3:
    print('Game is a draw')
elif winner == 0:
    print('The game is not over yet')
else:
    print(f'The winner is Player {winner}')