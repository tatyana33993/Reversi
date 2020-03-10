#!/usr/bin/env python3
import pygame


class Graphics:
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.pink = (255, 108, 173)
        self.blue = (0, 186, 254)
        self.margin = 5
        self.width = 60
        self.height = 60
        window_size = [525, 575]
        self.screen = pygame.display.set_mode(window_size)

    def draw_grid(self, game):
        self.screen.fill(self.black)

        for row in range(8):
            for column in range(8):
                color = self.white
                pygame.draw.rect(self.screen,
                                 color,
                                 [(self.margin + self.width)
                                  * column + self.margin,
                                  (self.margin + self.height)
                                  * row + self.margin,
                                  self.width,
                                  self.height])
        for row in range(8):
            for column in range(8):
                if game.grid[row][column] == 'X':
                    pygame.draw.ellipse(self.screen, self.pink,
                                        [(self.margin + self.width)
                                         * column + self.margin,
                                         (self.margin + self.height)
                                         * row + self.margin,
                                         60, 60])
                if game.grid[row][column] == 'O':
                    pygame.draw.ellipse(self.screen, self.blue,
                                        [(self.margin + self.width)
                                         * column + self.margin,
                                         (self.margin + self.height)
                                         * row + self.margin,
                                         60, 60])
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Pink:" + str(game.state['X'])
                           + " Blue:" + str(game.state['O']), True, self.white)
        self.screen.blit(text, [335, 540])
        if game.move_first and game.state['Empty'] != 0:
            font = pygame.font.SysFont('Calibri', 50, True, False)
            text = font.render("Player 1", True, self.white)
            self.screen.blit(text, [60, 520])
            pygame.draw.ellipse(self.screen, self.pink,
                                [250, 525, 40, 40])
        elif not game.move_first and game.state['Empty'] != 0:
            font = pygame.font.SysFont('Calibri', 50, True, False)
            text = font.render("Player 2", True, self.white)
            self.screen.blit(text, [60, 520])
            pygame.draw.ellipse(self.screen, self.blue,
                                [250, 525, 40, 40])
        if game.state['Empty'] == 0:
            if game.state['X'] > game.state['O']:
                font = pygame.font.SysFont('Calibri', 60, True, False)
                text = font.render("Good game!!!", True, self.black)
                self.screen.blit(text, [115, 210])
                font = pygame.font.SysFont('Calibri', 50, True, False)
                text = font.render("Winner pink!!!", True, self.white)
                self.screen.blit(text, [60, 520])
            elif game.state['X'] < game.state['O']:
                font = pygame.font.SysFont('Calibri', 60, True, False)
                text = font.render("Game over!!!", True, self.black)
                self.screen.blit(text, [115, 210])
                font = pygame.font.SysFont('Calibri', 50, True, False)
                text = font.render("Winer blue!!!", True, self.white)
                self.screen.blit(text, [60, 520])
            else:
                font = pygame.font.SysFont('Calibri', 60, True, False)
                text = font.render("You tried...", True, self.black)
                self.screen.blit(text, [115, 210])
                font = pygame.font.SysFont('Calibri', 50, True, False)
                text = font.render("Friendship", True, self.white)
                self.screen.blit(text, [60, 520])
