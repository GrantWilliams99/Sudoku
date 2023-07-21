# File Stuff

def get_filename():
    filename = input("Enter filename: ")
    return filename


def read_file(filename):
    file = open(filename, "r")
    initial_board = file.readlines()
    board = list(list())
    for line in initial_board:
        board.append(list(map(int, line.split(" "))))
    file.close()
    return board


def save_file(board, filename):
    file = open(filename, "w")
    for row in board:
        line = " ".join(map(str, row))
        file.write(line + "\n")
    file.close()