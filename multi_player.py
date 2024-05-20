from grid import print_grid
from logic import player_wins


def multi_player_game():
    player1_inputs = []
    player2_inputs = []
    player = "p1"
    game_over = False

    while not game_over:
        player_input = int(input("Enter position where you want to mark 'X' or 'O':"))

        if 1 <= player_input <= 9 and player_input - 1 not in player1_inputs and player_input - 1 not in player2_inputs:

            if player == "p1":
                player1_inputs.append(player_input - 1)
                player = "p2"
                print("Player 1 played:")
            else:
                player2_inputs.append(player_input - 1)
                player = "p1"
                print("Player 2 played:")
            print_grid(player1_inputs, player2_inputs)

            result = player_wins(player1_inputs, player2_inputs)
            if result != 0:
                game_over = True
                print(result)
            else:
                if len(player1_inputs) + len(player2_inputs) == 9:
                    game_over = True
                    print("It is a draw")

        else:
            game_over = True
