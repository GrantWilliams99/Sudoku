class Sudoku():
    def __init__(self, board):
        self.board = board
        self.rows = {0: set(), 1: set(), 2: set(),
                     3: set(), 4: set(), 5: set(),
                     6: set(), 7: set(), 8: set()}
        self.columns = {0: set(), 1: set(), 2: set(),
                        3: set(), 4: set(), 5: set(),
                        6: set(), 7: set(), 8: set()}
        self.boxes = {0: set(), 1: set(), 2: set(),
                      3: set(), 4: set(), 5: set(),
                      6: set(), 7: set(), 8: set()}
        
        # rows
        for i in range(9):
            self.rows[i] = set(self.board[i])
            if 0 in self.rows[i]:
                self.rows[i].remove(0)

        # columns
        for row in self.board:
            for i in range(9):
                self.columns[i].add(row[i])
        for i in range(9):
            if 0 in self.columns[i]:
                self.columns[i].remove(0)

        # boxes
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                box_index = (r // 3) * 3 + (c // 3)
                self.boxes[box_index].add(board[r][c])
        for i in range(9):
            if 0 in self.boxes[i]:
                self.boxes[i].remove(0)


    def display_board(self):
        print("    A B C | D E F | G H I")
        bar = "  +-------+-------+-------+"
        print(bar)

        for r in range(9):
            line = str(r + 1) + " "
            for c in range(9):
                if (c == 0):
                    line += "| "
                if (self.board[r][c] != 0):
                    line += str(self.board[r][c])
                else:
                    line += " "
                
                if (c in [2, 5, 8]):
                    line += " |"
                if (c != 8):
                    line += " "
            print(line)

            if (r == 2 or r == 5):
                print("--+-------+-------+-------+")

        print(bar)
    

    def is_valid_value(self, cell, number):
        if (number < 1 or number > 9):
            return False

        (row, col, box) = cell

        if number in self.rows[row] or number in self.columns[col] or number in self.boxes[box]:
            return False
        
        return True
    

    def is_open_cell(self, cell):
        (row, col, _) = cell
        return self.board[row][col] == 0
    

    def possible_values(self, cell):
        (row, col, box) = cell
        if self.is_open_cell(cell):
            complete = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            existing = self.rows[row] | self.columns[col] | self.boxes[box]
            difference = complete.difference(existing)
            return list(difference)
        else:
            return []
    

    def coordinate_to_cell(self, coordinate):
        row = int(coordinate[1]) - 1
        col = ord(coordinate[0]) - 65
        box = (row // 3) * 3 + (col // 3) 

        return (row, col, box)
    
    
    def edit_cell(self, cell, number):
        if (self.is_valid_value(cell, number)):
            (row, col, box) = cell

            # update the board and the three sets
            self.board[row][col] = number
            self.rows[row].add(number)
            self.columns[col].add(number)
            self.boxes[box].add(number)
        
            return True
        else:
            return False


    def solve(self):
        # naive solution
        while not self.is_complete():
            for row in range(9):
                for col in range(9):
                    box = (row // 3) * 3 + (col // 3)
                    cell = (row, col, box)
                    possible = self.possible_values(cell)
                    if len(possible) == 1:
                        self.edit_cell(cell, possible[0])
        self.display_board()


    def is_complete(self):
        # only need to check one dictionary 
        for i in range(9):
            if (len(list(self.rows[i])) < 9):
                return False
        
        return True
