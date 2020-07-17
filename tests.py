import unittest
from main import *


class TestGridSizeInput(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(is_valid_grid_size(""), False)

    def test_one_digit(self):
        self.assertEqual(is_valid_grid_size("5"), False)
        self.assertEqual(is_valid_grid_size("0"), False)

    def test_two_digits(self):
        self.assertEqual(is_valid_grid_size("67"), True)
        self.assertEqual(is_valid_grid_size("11"), True)
        self.assertEqual(is_valid_grid_size("99"), True)
        self.assertEqual(is_valid_grid_size("20"), False)
        self.assertEqual(is_valid_grid_size("02"), False)
        self.assertEqual(is_valid_grid_size("00"), False)

    def test_three_digits(self):
        self.assertEqual(is_valid_grid_size("111"), False)
        self.assertEqual(is_valid_grid_size("999"), False)

    def test_space(self):
        self.assertEqual(is_valid_grid_size("6 7"), False)


class TestPosAndDirectionInput(unittest.TestCase):
    grid_size = "99"

    def test_empty(self):
        self.assertEqual(is_valid_pos_and_direction("", self.grid_size), False)

    def test_one_digit(self):
        self.assertEqual(is_valid_pos_and_direction("1 E", self.grid_size), False)
        self.assertEqual(is_valid_pos_and_direction("0 E", self.grid_size), False)

    def test_two_digits(self):
        self.assertEqual(is_valid_pos_and_direction("11 N", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("99 N", self.grid_size), True)

    def test_three_digits(self):
        self.assertEqual(is_valid_pos_and_direction("111 N", self.grid_size), False)
        self.assertEqual(is_valid_pos_and_direction("999 N", self.grid_size), False)

    def test_zero(self):
        self.assertEqual(is_valid_pos_and_direction("10 N", self.grid_size), False)
        self.assertEqual(is_valid_pos_and_direction("09 N", self.grid_size), False)
        self.assertEqual(is_valid_pos_and_direction("00 N", self.grid_size), False)
        self.assertEqual(is_valid_pos_and_direction("000 N", self.grid_size), False)

    def test_direction(self):
        self.assertEqual(is_valid_pos_and_direction("12 ", self.grid_size), False)
        self.assertEqual(is_valid_pos_and_direction("12 N", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 E", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 S", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 W", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 n", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 e", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 s", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 w", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 North", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 East", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 South", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 West", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 north", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 east", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 south", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 west", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("12 q", self.grid_size), False)
        self.assertEqual(is_valid_pos_and_direction("12 southwest", self.grid_size), False)

    def test_space(self):
        self.assertEqual(is_valid_pos_and_direction("12N", self.grid_size), False)
        self.assertEqual(is_valid_pos_and_direction("N", self.grid_size), False)

    def test_pos_in_grid(self):
        self.assertEqual(is_valid_pos_and_direction("11 N", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("88 N", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("99 N", self.grid_size), True)
        self.assertEqual(is_valid_pos_and_direction("36 N", "55"), False)
        self.assertEqual(is_valid_pos_and_direction("63 N", "55"), False)


class TestInstructionsInput(unittest.TestCase):
    grid = Grid()
    rover = Rover()
    rover.set_grid(grid)

    def test_empty(self):
        self.rover.set_instructions("")
        self.assertEqual(self.rover.is_valid_instructions(), False)

    def test_north(self):
        self.rover.get_grid().set_dimensions(5, 5)
        self.rover.set_direction("N")
        self.rover.set_position(3, 3)

        self.rover.set_instructions("MMM")
        self.assertEqual(self.rover.is_valid_instructions(), False)

        self.rover.set_instructions("MM")
        self.assertEqual(self.rover.is_valid_instructions(), True)

    def test_south(self):
        self.rover.get_grid().set_dimensions(5, 5)
        self.rover.set_direction("S")
        self.rover.set_position(3, 3)

        self.rover.set_instructions("MMM")
        self.assertEqual(self.rover.is_valid_instructions(), False)

        self.rover.set_instructions("MM")
        self.assertEqual(self.rover.is_valid_instructions(), True)

    def test_east(self):
        self.rover.get_grid().set_dimensions(5, 5)
        self.rover.set_direction("E")
        self.rover.set_position(3, 3)

        self.rover.set_instructions("MMM")
        self.assertEqual(self.rover.is_valid_instructions(), False)

        self.rover.set_instructions("MM")
        self.assertEqual(self.rover.is_valid_instructions(), True)

    def test_west(self):
        self.rover.get_grid().set_dimensions(5, 5)
        self.rover.set_direction("W")
        self.rover.set_position(3, 3)

        self.rover.set_instructions("MMM")
        self.assertEqual(self.rover.is_valid_instructions(), False)

        self.rover.set_instructions("MM")
        self.assertEqual(self.rover.is_valid_instructions(), True)

    def test_move_and_rotate(self):
        self.rover.get_grid().set_dimensions(5, 5)
        self.rover.set_position(3, 3)

        self.rover.set_direction("N")
        self.rover.set_instructions("M")
        self.rover.execute_instructions(render=False)
        self.assertEqual(self.rover.get_position(), (3, 4))
        self.assertEqual(self.rover.get_direction(), "N")

        self.rover.set_direction("N")
        self.rover.set_position(3, 3)
        self.rover.set_instructions("R")
        self.rover.execute_instructions(render=False)
        self.assertEqual(self.rover.get_position(), (3, 3))
        self.assertEqual(self.rover.get_direction(), "E")

        self.rover.set_direction("N")
        self.rover.set_position(3, 3)
        self.rover.set_instructions("L")
        self.rover.execute_instructions(render=False)
        self.assertEqual(self.rover.get_position(), (3, 3))
        self.assertEqual(self.rover.get_direction(), "W")

    def test_edge_cases(self):
        self.rover.get_grid().set_dimensions(1, 1)
        self.rover.set_position(1, 1)
        self.rover.set_direction("E")
        self.rover.set_instructions("L")
        self.rover.execute_instructions(render=False)
        self.assertEqual(self.rover.get_position(), (1, 1))
        self.assertEqual(self.rover.get_direction(), "N")

        self.rover.get_grid().set_dimensions(9, 9)
        self.rover.set_position(9, 9)
        self.rover.set_direction("S")
        self.rover.set_instructions("R")
        self.rover.execute_instructions(render=False)
        self.assertEqual(self.rover.get_position(), (9, 9))
        self.assertEqual(self.rover.get_direction(), "W")

        self.rover.get_grid().set_dimensions(1, 5)
        self.rover.set_position(1, 3)
        self.rover.set_direction("E")
        self.rover.set_instructions("L")
        self.rover.execute_instructions(render=False)
        self.assertEqual(self.rover.get_position(), (1, 3))
        self.assertEqual(self.rover.get_direction(), "N")

        self.rover.get_grid().set_dimensions(5, 1)
        self.rover.set_position(3, 1)
        self.rover.set_direction("E")
        self.rover.set_instructions("L")
        self.rover.execute_instructions(render=False)
        self.assertEqual(self.rover.get_position(), (3, 1))
        self.assertEqual(self.rover.get_direction(), "N")

    def test_other_cases(self):
        self.rover.get_grid().set_dimensions(8, 8)
        self.rover.set_position(1, 2)
        self.rover.set_direction("E")
        self.rover.set_instructions("MMLMRMMRRMML")
        self.rover.execute_instructions(render=False)
        self.assertEqual(self.rover.get_position(), (3, 3))
        self.assertEqual(self.rover.get_direction(), "S")

        self.rover.get_grid().set_dimensions(7, 6)
        self.rover.set_position(3, 4)
        self.rover.set_direction("S")
        self.rover.set_instructions("MLMRMLMRMRRMMM")
        self.rover.execute_instructions(render=False)
        self.assertEqual(self.rover.get_position(), (5, 4))
        self.assertEqual(self.rover.get_direction(), "N")

        self.rover.get_grid().set_dimensions(5, 5)
        self.rover.set_position(1, 5)
        self.rover.set_direction("S")
        self.rover.set_instructions("MMMMLMMMM")
        self.rover.execute_instructions(render=False)
        self.assertEqual(self.rover.get_position(), (5, 1))
        self.assertEqual(self.rover.get_direction(), "E")

        self.rover.get_grid().set_dimensions(5, 5)
        self.rover.set_position(1, 1)
        self.rover.set_direction("N")
        self.rover.set_instructions("MRMLMRMLMRMLMRML")
        self.rover.execute_instructions(render=False)
        self.assertEqual(self.rover.get_position(), (5, 5))
        self.assertEqual(self.rover.get_direction(), "N")


if __name__ == "__main__":
    unittest.main()
