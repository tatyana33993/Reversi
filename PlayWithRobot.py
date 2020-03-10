#!/usr/bin/env python3
import pygame
from Game import Game
from Player import Player
from Robot import Robot
from Graphics import Graphics


class Play:
    def play_game(self):
        game = Game('X', 'O')
        player = Player()
        robot = Robot()

        pygame.init()
        graphics = Graphics()
        pygame.display.set_caption("Reversi Game")

        done = False

        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN and game.move_first:
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (graphics.width + graphics.margin)
                    row = pos[1] // (graphics.height + graphics.margin)
                    if game.in_grid(row, column)\
                            and (game.grid[row][column] == ''):
                        if player.do_correct_move_player(game, row, column,
                                                         game.player,
                                                         game.rival)\
                                is not False:
                            game.move_first = False
                elif not game.move_first:
                    x, y = robot.get_best_move_robot(game)
                    robot.do_move_robot(game, x, y)
                    game.move_first = True
                else:
                    pass
                scores = game.get_score_of_grid(game.grid)
                game.state['X'] = scores['X']
                game.state['O'] = scores['O']
                game.state['Empty'] = 64 - scores['X'] - scores['O']

            graphics.draw_grid(game)

            clock.tick(60)

            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    play = Play()
    play.play_game()
