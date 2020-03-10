#!/usr/bin/env python3


class Player:
    def do_correct_move_player(self, game, row, column, chip, opponent_chip):
        if not game.is_valid_move(row, column, chip, opponent_chip):
            return False

        while True:
            grid_with_move = game.make_move(game.grid, row, column,
                                            chip, opponent_chip)
            if not grid_with_move:
                game.grid = grid_with_move
            else:
                break
