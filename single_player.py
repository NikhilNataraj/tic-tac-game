from grid import print_grid
from logic import player_wins
from ai_logic import ai_gameplay


def single_player_game():
    player1_inputs = []
    ai = []
    player = "p1"
    game_over = False

    while not game_over:
        if player == "p1":
            player_input = int(input("Enter position where you want to mark 'X' or 'O':"))

            if 1 <= player_input <= 9 and player_input - 1 not in player1_inputs and player_input - 1 not in ai:
                player1_inputs.append(player_input - 1)
                player = "ai"
                print("You played:")
        else:
            ai_input = ai_gameplay(player1_inputs, ai)
            ai.append(ai_input - 1)
            player = "p1"
            print("AI plays:")

        print_grid(player1_inputs, ai)
        print()

        result = player_wins(player1_inputs, ai)
        if result != 0:
            game_over = True
            print(result)
        else:
            if len(player1_inputs) + len(ai) == 9:
                game_over = True
                print("It is a draw")
