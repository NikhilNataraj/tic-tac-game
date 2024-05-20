import random

# All possible winning combinations
WINS = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
        [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def ai_gameplay(player1_inputs, ai_input):
    # For first turn generating a random integer which is not played by the user.
    if len(ai_input) == 0:
        ai_pos = random.randint(1, 9)
        while ai_pos in player1_inputs or ai_pos in ai_input:
            ai_pos = random.randint(1, 9)
        return ai_pos

    # if this is second turn
    else:
        player1_inputs.sort()
        ai_input.sort()

        # Creating a dictionary of all winning combinations of the user
        player_win_poss = {}
        for item in player1_inputs:
            for win_index in range(len(WINS)):
                win = WINS[win_index]
                if item in win:
                    if win_index in player_win_poss:
                        player_win_poss[win_index] += 1
                    else:
                        player_win_poss[win_index] = 1

        # Creating a dictionary of all winning combinations of the ai
        ai_win_poss = {}
        for item in ai_input:
            for win_index in range(len(WINS)):
                win = WINS[win_index]
                if item in win:
                    if win_index in ai_win_poss:
                        ai_win_poss[win_index] += 1
                    else:
                        ai_win_poss[win_index] = 1

        # Combining both the dictionaries
        ai_win_poss.update(player_win_poss)

        # Remove keys where all positions are already played
        all_plays = ai_input + player1_inputs
        for key in list(ai_win_poss.keys()):
            win = WINS[key]
            if all(pos in all_plays for pos in win):
                del ai_win_poss[key]

        if ai_win_poss:
            # Getting the index of the win which has max possibility
            max_win_poss = list(ai_win_poss.keys())[
                list(ai_win_poss.values()).index(max(ai_win_poss.values()))]

            # Loop to check which pos is empty
            for i in WINS[max_win_poss]:
                if i not in all_plays:
                    return i + 1

        else:
            # If ai_win_poss is empty, choose a random position
            available_positions = [pos for pos in range(9) if pos not in all_plays]
            return random.choice(available_positions) + 1
