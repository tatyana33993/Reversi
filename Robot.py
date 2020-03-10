#!/usr/bin/env python3


class Robot:
    def get_best_move_robot(self, game):
        valid_moves = game.get_valid_moves(game.rival, game.player)
        for x, y in valid_moves:
            if game.is_on_corner(x, y) and game.grid[x][y] == '':
                return [x, y]

        best_score = -1
        best_move = [-1, -1]
        for x, y in valid_moves:
            if game.grid[x][y] == '':
                copy_grid = game.get_grid_copy()
                copy_grid_with_move = game.make_move(copy_grid, x, y,
                                                     game.rival, game.player)
                score = game.get_score_of_grid(copy_grid_with_move)[game.rival]
                if score > best_score:
                    best_move = [x, y]
                    best_score = score
        return best_move

    def get_random_move_robot(self, game):
        valid_moves = game.get_valid_moves(game.rival, game.player)
        for x, y in valid_moves:
            if game.grid[x][y] == '':
                return [x, y]

    def do_move_robot(self, game, x, y):
        while True:
            if not game.make_move(game.grid, x, y, game.rival, game.player):
                continue
            else:
                break
