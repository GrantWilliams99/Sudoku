from sudoku import Sudoku as Sudoku
from file import *

def get_cell():
    coordinate = "  "
    valid_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    
    while True:
        coordinate = input("Enter coordinate: ")
        if coordinate[0] in valid_letters and int(coordinate[1]) > 0 and int(coordinate[1]) < 10:
            break

    row = int(coordinate[1]) - 1
    col = ord(coordinate[0]) - 65
    box = (row // 3) * 3 + (col // 3)
    
    return (row, col, box)


def get_number():
    number = 0

    while True:
        number = int(input("Enter number: "))
        if number > 0 and number < 10:
            break

    return number


def display_options():
    print("Options:")
    print("   ?  Show Instructions")
    print("   D  Display Board")
    print("   E  Edit Square")
    print("   S  Show Possible Values")
    print("   !  Solve the Board")
    print("   Q  Save and Quit")


def interact(game):
    display_options()
    game.display_board()
    command = ""

    while command != "Q":

        command = str(input("> "))

        match command:
            case "?": 
                display_options()
            case "D": 
                game.display_board()
            case "E": 
                cell = get_cell()
                number = get_number()
                game.edit_cell(cell, number)
            case "S":
                cell = get_cell()
                print(game.possible_values(cell))
            case "!":
                game.solve()
            case "C":
                print(game.is_complete())
            case "Q":
                break


def main():
    filename = get_filename()
    board = read_file(filename)
    game = Sudoku(board)
    interact(game)
    save_file(board, "test.txt")


if __name__ == '__main__':
    main()
