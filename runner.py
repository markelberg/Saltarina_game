import pygame
import sys

from settings import Settings


class Runner:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('RUNNER')
        self.clock = pygame.time.Clock()
        self.game_active = True

        self.font = pygame.font.Font('font/pixeltype.ttf', 50)
        self.text = self.font.render('Ilene  saltarina', False, 'Purple')
        self.text_rect = self.text.get_rect(center = (400, 100))

        self.sky_surface = pygame.image.load('graphics/sky.png').convert()
        self.ground_surface = pygame.image.load('graphics/ground.png').convert()

        self.snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
        self.snail_rect = self.snail.get_rect(midbottom=(600, 400))
        self.player = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        self.player_rect = self.player.get_rect(midbottom=(80, 400))
        self.player_gravity = 0

    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self._graphics_()
                self._gravity_()
                self._collision_()
            else:
                self.screen.fill('red')
            pygame.display.update()
            self.clock.tick(60)  # How many frames per second

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.game_active:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.player_rect.collidepoint(event.pos):
                        self.player_gravity = -20
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.player_rect.bottom >= 400:
                        self.player_gravity = -20
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP or pygame.K_KP_ENTER:
                    self.game_active = True
                    self.snail_rect.left = 800
    def _graphics_(self):
        self.screen.blit(self.sky_surface, (0, 0))
        self.screen.blit(self.ground_surface, (0, 400))
        #pygame.draw.rect(self.screen, 'Pink', self.text_rect)
        self.screen.blit(self.text, self.text_rect)

        self.snail_rect.x -= 4
        if self.snail_rect.right <= 0:
            self.snail_rect.left = 800
        self.screen.blit(self.snail, self.snail_rect)
        self.screen.blit(self.player, self.player_rect)

    def _gravity_(self):
        self.player_gravity += 1
        self.player_rect.y += self.player_gravity
        if self.player_rect.bottom >= 400:
            self.player_rect.bottom = 400
        self.screen.blit(self.player, self.player_rect)

    def _collision_(self):
        if self.snail_rect.colliderect(self.player_rect):
            self.game_active = False


if __name__ == '__main__':
    runner = Runner()
    runner.run_game()