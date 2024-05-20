WINS = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
        [1, 4, 7], [2, 5 ,8], [0, 4, 8], [2, 4,6]]


def player_wins(p1, p2):
    p1.sort()
    p2.sort()
    for win in WINS:
        if set(win) <= set(p1):
            return "P1 wins!\n"
        elif set(win) <= set(p2):
            return "P2 wins!\n"
    return 0


