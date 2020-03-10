#!/usr/bin/env python3
import pygame
import socket
from Game import Game
from Player import Player
from Graphics import Graphics


class Play:
    def play_game(self):
        game = Game('X', 'O')
        player = Player()

        sock = socket.socket()
        sock.bind(("", 1024))
        sock.listen(1)
        conn, addr = sock.accept()

        pygame.init()
        graphics = Graphics()
        pygame.display.set_caption("Reversi Game")

        done = False

        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    conn.close()
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
                            x = '{0} {1}'.format(column, row)
                            conn.send(x.encode("utf-8"))
                elif not game.move_first:
                    data = conn.recv(16384)
                    udata = data.decode('utf-8')
                    arr = udata.split(' ')
                    column = int(arr[0])
                    row = int(arr[1])
                    if player.do_correct_move_player(game, row, column,
                                                     game.rival,
                                                     game.player) is not False:
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
