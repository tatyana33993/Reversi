#!/usr/bin/env python3

from Game import Game
from Player import Player
from Robot import Robot
import unittest


class GameTest(unittest.TestCase):
    def test_create_grid(self):
        game = Game('X', 'O')
        grid = game.create_grid()
        self.assertEqual(len(grid), 8)

    def test_initialize_grid_one(self):
        game = Game('X', 'O')
        self.assertEqual(game.grid[3][3], 'X')
        self.assertEqual(game.grid[4][4], 'X')

    def test_initialize_grid_two(self):
        game = Game('X', 'O')
        self.assertEqual(game.grid[3][4], 'O')
        self.assertEqual(game.grid[4][3], 'O')

    def test_get_grid_copy_one(self):
        game = Game('X', 'O')
        copy_grid = game.get_grid_copy()
        self.assertEqual(len(copy_grid), 8)

    def test_get_grid_copy_two(self):
        game = Game('X', 'O')
        copy_grid = game.get_grid_copy()
        self.assertEqual(copy_grid[3][3], 'X')
        self.assertEqual(copy_grid[4][4], 'X')

    def test_get_grid_copy_three(self):
        game = Game('X', 'O')
        copy_grid = game.get_grid_copy()
        self.assertEqual(copy_grid[3][4], 'O')
        self.assertEqual(copy_grid[4][3], 'O')

    def test_in_grid_upper_left(self):
        game = Game('X', 'O')
        result = game.in_grid(-1, 0)
        self.assertFalse(result)

    def test_in_grid_upper_right(self):
        game = Game('X', 'O')
        result = game.in_grid(8, 0)
        self.assertFalse(result)

    def test_in_grid_lower_left(self):
        game = Game('X', 'O')
        result = game.in_grid(-1, 7)
        self.assertFalse(result)

    def test_in_grid_lower_right(self):
        game = Game('X', 'O')
        result = game.in_grid(8, 7)
        self.assertFalse(result)

    def test_in_grid_center(self):
        game = Game('X', 'O')
        result = game.in_grid(3, 3)
        self.assertTrue(result)

    def test_is_on_corner_one(self):
        game = Game('X', 'O')
        result = game.is_on_corner(0, 0)
        self.assertTrue(result)

    def test_is_on_corner_two(self):
        game = Game('X', 'O')
        result = game.is_on_corner(7, 0)
        self.assertTrue(result)

    def test_is_on_corner_three(self):
        game = Game('X', 'O')
        result = game.is_on_corner(0, 7)
        self.assertTrue(result)

    def test_is_on_corner_four(self):
        game = Game('X', 'O')
        result = game.is_on_corner(7, 7)
        self.assertTrue(result)

    def test_is_on_corner_five(self):
        game = Game('X', 'O')
        result = game.is_on_corner(4, 4)
        self.assertFalse(result)

    def test_create_state_one(self):
        game = Game('X', 'O')
        self.assertEqual(game.state['Empty'], 60)

    def test_create_state_two(self):
        game = Game('X', 'O')
        self.assertEqual(game.state['X'], 2)

    def test_create_state_three(self):
        game = Game('X', 'O')
        self.assertEqual(game.state['O'], 2)

    def test_get_score_of_grid(self):
        game = Game('X', 'O')
        scores = game.get_score_of_grid(game.grid)
        self.assertEqual(scores['X'], 2)
        self.assertEqual(scores['O'], 2)

    def test_is_valid_move_true_x(self):
        game = Game('X', 'O')
        self.assertTrue(game.is_valid_move(3, 5, 'X', 'O') is not False)

    def test_is_valid_move_true_o(self):
        game = Game('X', 'O')
        self.assertTrue(game.is_valid_move(3, 2, 'O', 'X') is not False)

    def test_is_valid_move_false_x(self):
        game = Game('X', 'O')
        self.assertFalse(game.is_valid_move(3, 2, 'X', 'O'))

    def test_is_valid_move_false_o(self):
        game = Game('X', 'O')
        self.assertFalse(game.is_valid_move(3, 5, 'O', 'X'))

    def test_get_valid_moves_x(self):
        game = Game('X', 'O')
        moves = game.get_valid_moves('X', 'O')
        for e in moves:
            self.assertTrue(game.is_valid_move(e[0], e[1], 'X', 'O')
                            is not False)

    def test_get_valid_moves_o(self):
        game = Game('X', 'O')
        moves = game.get_valid_moves('O', 'X')
        for e in moves:
            self.assertTrue(game.is_valid_move(e[0], e[1], 'O', 'X')
                            is not False)

    def test_make_move(self):
        game = Game('X', 'O')
        copy_grid = game.get_grid_copy()
        game.make_move(copy_grid, 3, 5, 'X', 'O')
        self.assertTrue(copy_grid[3][5] == 'X')
        self.assertTrue(copy_grid[3][4] == 'X')

    def test_player_x(self):
        game = Game('X', 'O')
        player = Player()
        player.do_correct_move_player(game, 3, 5, 'X', 'O')
        self.assertTrue(game.grid[3][5] == 'X')
        self.assertTrue(game.grid[3][4] == 'X')

    def test_player_o(self):
        game = Game('X', 'O')
        player = Player()
        player.do_correct_move_player(game, 3, 2, 'O', 'X')
        self.assertTrue(game.grid[3][2] == 'O')
        self.assertTrue(game.grid[3][3] == 'O')

    def test_player_false(self):
        game = Game('X', 'O')
        player = Player()
        self.assertFalse(player.do_correct_move_player(game, 3, 2, 'X', 'O'))

    def test_robot_best(self):
        game = Game('X', 'O')
        robot = Robot()
        score = game.get_score_of_grid(game.grid)
        x, y = robot.get_best_move_robot(game)
        robot.do_move_robot(game, x, y)
        new_score = game.get_score_of_grid(game.grid)
        self.assertTrue(score['O'] < new_score['O'])

    def test_robot_random(self):
        game = Game('X', 'O')
        robot = Robot()
        score = game.get_score_of_grid(game.grid)
        x, y = robot.get_random_move_robot(game)
        robot.do_move_robot(game, x, y)
        new_score = game.get_score_of_grid(game.grid)
        self.assertTrue(score['O'] < new_score['O'])


if __name__ == '__main__':
    unittest.main()
