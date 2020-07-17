from itertools import cycle, islice


class Rover:
    def __init__(self):
        self.row = -1
        self.col = -1
        self.direction = ""
        self.instructions = ""
        self.move_directions = {"W": (-1, 0), "N": (0, 1), "E": (1, 0), "S": (0, -1)}
        self.grid = None

    def get_position(self):
        return self.row, self.col

    def get_direction(self):
        return self.direction

    def get_instructions(self):
        return self.instructions

    def get_grid(self):
        return self.grid

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def set_direction(self, direction):
        self.direction = direction

    def set_instructions(self, instructions):
        self.instructions = instructions

    def set_grid(self, grid):
        self.grid = grid

    def is_valid_instructions(self):
        if self.instructions == "":
            print("Instructions are empty.")
            return False

        grid_row, grid_col = self.get_grid().get_dimensions()
        row, col = self.get_position()
        direction = self.get_direction()
        instructions = self.get_instructions()
        result = True

        while self.has_next_instruction():
            print(self.get_position(), self.get_direction(), self.grid.get_dimensions())
            self.do_next_instruction()
            if self.col > grid_col:
                result = False
                print("\tInvalid instructions.\n\tRover will move too far North.")
                break
            elif self.col <= 0:
                result = False
                print("\tInvalid instructions.\n\tRover will move too far South.")
                break
            elif self.row > grid_row:
                result = False
                print("\tInvalid instructions.\n\tRover will move too far East.")
                break
            elif self.row <= 0:
                result = False
                print("\tInvalid instructions.\n\tRover will move too far West.")
                break

        self.set_position(row, col)
        self.set_direction(direction)
        self.set_instructions(instructions)
        return result

    def _rotate(self, dirs):
        index = dirs.index(self.direction)
        dirs = cycle(dirs)
        dirs = islice(dirs, index + 1, None)
        self.direction = next(dirs)

    def rotate_left(self):
        dirs = ["N", "W", "S", "E"]
        self._rotate(dirs)

    def rotate_right(self):
        dirs = ["N", "E", "S", "W"]
        self._rotate(dirs)

    def move(self):
        step_direction = self.move_directions[self.direction]
        self.row += step_direction[0]
        self.col += step_direction[1]

    def has_next_instruction(self):
        return len(self.instructions) > 0

    def do_next_instruction(self):
        if self.has_next_instruction():
            curr_instruction = self.instructions[0]
            self.instructions = self.instructions[1:]
            if curr_instruction == "M":
                self.move()
            elif curr_instruction == "L":
                self.rotate_left()
            elif curr_instruction == "R":
                self.rotate_right()

    def execute_instructions(self, render=True):
        if render:
            self.grid.render_grid(self.row, self.col, self.direction, self.get_instructions())
        while self.has_next_instruction():
            self.do_next_instruction()
            if render:
                self.grid.render_grid(self.row, self.col, self.direction, self.get_instructions())
