import time
from helpers_and_functions.function_helpers import *
from helpers_and_functions.buttons_to_use.buttons_to_use_dino import *
from images.dino_images import *


class Dino:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        back = pygame.image.load("images/dino_images/dino_backgruond.png")
        self.back = pygame.transform.scale(back, (WIDTH * 10, HEIGHT))
        enemy = pygame.image.load("images/dino_images/y.png")
        self.enemy = pygame.transform.scale(enemy, (WIDTH_ENEMY, HEIGHT_ENEMY))
        player = pygame.image.load("images/dino_images/dino_player.png").convert()
        player.set_colorkey((255, 255, 255))
        self.player = pygame.transform.scale(player, (WIDTH_PLAYER, HEIGHT_PLAYER))
        self.font = pygame.font.SysFont('bahnschrift', round(WIDTH / 70) + round(HEIGHT / 70))

    def home_screen(self):
        self.screen.fill((255, 255, 255))
        fin = False
        while not fin:
            add_image(self.screen, "images/dino_images/open_back.gif", 0, 0, WIDTH, HEIGHT, None)
            add_image(self.screen, "images/dino_images/start_button.png.crdownload", START_BUTTON_X, START_BUTTON_Y,
                      START_BUTTON_WIDTH, START_BUTTON_HEIGHT, None)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if mouse_in_button(start_button, pos):
                        self.game_screen()

            pygame.display.flip()

    def game_screen(self):
        finish = False

        start_time = time.time()
        add_enemy = False
        refresh_rate = 200
        level = 1
        x_pos = 0
        x_enemy = X_ENEMY_START
        y_player = Y_PLAYER
        isJump = False
        side = False

        clock = pygame.time.Clock()
        while not finish:
            current_time = time.time()
            text = self.font.render(str(round(current_time - start_time)), True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (round(WIDTH / 1.09), round(HEIGHT / 16))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finish = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and not isJump:
                        isJump = True
            self.screen.blit(self.back, (x_pos, 0))
            self.screen.blit(text, textRect)
            if x_enemy == X_PLAYER + round(WIDTH_PLAYER / 2) and y_player == Y_PLAYER:
                finish = True
            if isJump:
                if y_player > PLAYER_JUMP_MAX_HEIGHT and not side:
                    y_player -= 2
                else:
                    side = True
                    y_player += 2
                if y_player == Y_PLAYER:
                    isJump = False
                    side = False
            if not add_enemy:
                add_enemy = True
            if add_enemy and x_pos < 0:
                if x_enemy < -1 * WIDTH_ENEMY:
                    add_enemy = False
                    x_enemy = X_ENEMY_START

                else:
                    self.screen.blit(self.enemy, (x_enemy, Y_ENEMY))
                    x_enemy -= 1
            self.screen.blit(self.player, (X_PLAYER, y_player))

            if x_pos != -(WIDTH * 9):
                x_pos -= 1
            else:
                x_pos = 0
                x_enemy += 3
                add_enemy = False

            if level == 1000:
                refresh_rate += 5
                level = 0
            else:
                level += 1
            pygame.display.update()
            clock.tick(refresh_rate)
