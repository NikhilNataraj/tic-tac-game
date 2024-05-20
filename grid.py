def print_line():
    print("|", end=" ")


def print_dashes():
    for _ in range(8):
        print("_", end=" ")


def print_grid(p1, p2):
    p1.sort()
    p2.sort()
    index = 0
    for r in range(3):
        print(" ", end=" ")
        for c in range(3):
            if index in p1:
                print("X", end=" ")
            elif index in p2:
                print("O", end=" ")
            else:
                print(" ", end=" ")

            if c < 2:
                print_line()

            index += 1
        print()
        print_dashes()
        print()
