#!/usr/bin/env python3


class Game:
    def __init__(self, player_chip, rival_chip):

        self.grid = self.create_grid()
        self.initialize_grid()
        self.state = {'Empty': 60, 'X': 2, 'O': 2}
        self.move_first = True
        self.player = player_chip
        self.rival = rival_chip

    def create_grid(self):
        grid = []
        for row in range(8):
            grid.append([])
            for column in range(8):
                grid[row].append('')
        return grid

    def initialize_grid(self):
        self.grid[3][3] = 'X'
        self.grid[3][4] = 'O'
        self.grid[4][3] = 'O'
        self.grid[4][4] = 'X'

    def get_grid_copy(self):
        copy_grid = self.create_grid()
        for x in range(8):
            for y in range(8):
                copy_grid[x][y] = self.grid[x][y]
        return copy_grid

    def in_grid(self, x, y):
        return (x >= 0) and (x <= 7) and (y >= 0) and (y <= 7)

    def is_on_corner(self, x, y):
        return (x == 0 and y == 0) or (x == 7 and y == 0)\
               or (x == 0 and y == 7) or (x == 7 and y == 7)

    def get_score_of_grid(self, grid):
        xscore = 0
        oscore = 0
        for x in range(8):
            for y in range(8):
                if grid[x][y] == 'X':
                    xscore += 1
                if grid[x][y] == 'O':
                    oscore += 1
        return {'X': xscore, 'O': oscore}

    def is_valid_move(self, row, column, chip, opponent_chip):
        chips_to_flip = []
        increments = [[-1, -1], [1, -1], [-1, 1], [1, 1],
                      [0, 1], [1, 0], [0, -1], [-1, 0]]
        for i, j in increments:
            x, y = row, column
            x += i
            y += j
            if self.in_grid(x, y) and self.grid[x][y] == opponent_chip:
                x += i
                y += j
                if not self.in_grid(x, y):
                    continue
                while self.grid[x][y] == opponent_chip:
                    x += i
                    y += j
                    if not self.in_grid(x, y):
                        break
                if not self.in_grid(x, y):
                    continue
                if self.grid[x][y] == chip:
                    while True:
                        x -= i
                        y -= j
                        if x == row and y == column:
                            break
                        chips_to_flip.append([x, y])
        if len(chips_to_flip) == 0:
            return False
        else:
            return chips_to_flip

    def get_valid_moves(self, chip, opponent_chip):
        valid_moves = []
        for x in range(8):
            for y in range(8):
                if self.is_valid_move(x, y, chip, opponent_chip):
                    valid_moves.append([x, y])
        return valid_moves

    def make_move(self, grid, row, column, chip, opponent_chip):
        chips_to_flip = self.is_valid_move(row, column, chip, opponent_chip)
        if chips_to_flip is False:
            return False

        grid[row][column] = chip
        for x, y in chips_to_flip:
            grid[x][y] = chip
        return grid
