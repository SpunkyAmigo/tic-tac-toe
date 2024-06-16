from lib import TTTConfidentAI, TTTHopelessAI, TTTRandom, TTTHuman
from game import TicTacToe

def main():
    options = [
        'TTTConfidentAI',
        'TTTHopelessAI',
        'TTTRandom',
        'TTTHuman',
        'Exit'
    ]

    for i, option in enumerate(options):
        print(f'{i+1}. {option}')
    
    choice_message = 'Choose an option: '

    players = []
    while len(players) < 2:
        player = None
        player_number = len(players) + 1
        choice = input(choice_message)
        if choice == '1':
            player = TTTConfidentAI(player_number)
        elif choice == '2':
            player = TTTHopelessAI(player_number)
        elif choice == '3':
            player = TTTRandom()
        elif choice == '4':
            player = TTTHuman()
        elif choice == '5':
            # Exit
            return
        else:
            # Invalid input
            continue
        players.append(player)

    random_iterations_message = 'Enter number of random iterations: '
    random_iterations = input(random_iterations_message)
    # Make sure input is a positive integer
    while not random_iterations.isdigit() or int(random_iterations) < 0:
        random_iterations = input(random_iterations_message)

    random_iterations = int(random_iterations)

    game = TicTacToe(players[0], players[1], random_iterations=random_iterations)
    game.play()




if __name__ == '__main__':
    main()
