from file import *
from sudoku import Sudoku as Sudoku

game = Sudoku(read_file("0.txt"))

def run_all():
    test_coordinate_to_cell()

def test_coordinate_to_cell():
	print("coordinate_to_cell()")

	# Test 1
	test = "Happy Path"
	expected = (4, 4, 4)
	actual = game.coordinate_to_cell("E5")
	if expected == actual:
		print(test, "passed")
	else:
		print(test, "failed")

	# Test 2
	test = "Invalid Coordinate"
	expected = ()