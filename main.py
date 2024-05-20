import grid
from multi_player import multi_player_game
from single_player import single_player_game

play = True

while play:

    gameplay = int(input("Do you want to play\n1. Single Player\n2. Multi Player\n3. Quit\n"
                         "Enter 1, 2 or 3:"))

    if gameplay != 3:
        index = 0
        for r in range(3):
            print(" ", end=" ")
            for c in range(3):
                print(index+1, end=" ")

                if c < 2:
                    grid.print_line()

                index += 1
            print()
            grid.print_dashes()
            print()

    if gameplay == 2:
        multi_player_game()

    elif gameplay == 1:
        single_player_game()

    else:
        play = False

