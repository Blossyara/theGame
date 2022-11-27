import pygame
import sys


#SETTINGS
WIDTH = 1280
HEIGHT = 800
AQUAMARINE = (0, 0, 255)
BLACK = (0, 0, 0)
CHECK = (255, 0, 100)
SPEED = 5
FPS = 60

#TEXTURES parameters
MAP_SIZE = (50, 25)
TEXTURE_SIZE = 25

#WINDOW_FRAME parameters
WINDOW_FRAME_border = round(WIDTH*0.01, -1) - 5
WINDOW_FRAME_thick = 10
WINDOW_FRAME_width = MAP_SIZE[0] * TEXTURE_SIZE + 2 * WINDOW_FRAME_thick
WINDOW_FRAME_height = MAP_SIZE[1] * TEXTURE_SIZE + 2 * WINDOW_FRAME_thick


class Character():
    def __init__(self, screen):
        #pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('IMAGES/test_image.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centery-50
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_person(self):
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += SPEED
        if self.mleft and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= SPEED
        if self.mup and self.rect.top > self.screen_rect.top:
            self.rect.bottom -= SPEED
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += SPEED


def events(person): # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                person.mright = True
            if event.key == pygame.K_a:
                person.mleft = True
            if event.key == pygame.K_s:
                person.mdown = True
            if event.key == pygame.K_w:
                person.mup = True

            if event.key == pygame.K_1: # size test
                print('Размер внутреннего игрового окна:', GAME_ZONE.size,
                      'Левый угол: ', GAME_ZONE.topleft,
                      'Правый угол: ', GAME_ZONE.topright)
                print('Размер внешнего окна: ', WINDOW.size,
                      'Левый угол: ', WINDOW.topleft,
                      'Правый угол: ', WINDOW.bottomright)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                person.mright = False
            if event.key == pygame.K_a:
                person.mleft = False
            if event.key == pygame.K_s:
                person.mdown = False
            if event.key == pygame.K_w:
                person.mup = False


def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) #pygame.FULLSCREEN
    pygame.display.set_caption("NAMENAMENAME")
    SCREEN.fill(AQUAMARINE)


    WINDOW = pygame.draw.rect(SCREEN, BLACK, (WINDOW_FRAME_border,
                                              WINDOW_FRAME_border,
                                              WINDOW_FRAME_width,
                                              WINDOW_FRAME_height), 10)
    GAME_ZONE = pygame.draw.rect(SCREEN, CHECK, (WINDOW_FRAME_border + WINDOW_FRAME_thick,
                                            WINDOW_FRAME_border + WINDOW_FRAME_thick,
                                            WINDOW_FRAME_width - 2*WINDOW_FRAME_thick,
                                            WINDOW_FRAME_height-2*WINDOW_FRAME_thick))

    GRASS = pygame.image.load('IMAGES/grass.png').convert_alpha() # size 25x25


    clock = pygame.time.Clock()
    Mirosha = Character(SCREEN)
    pygame.display.update()
    while True:
        textured_mash = pygame.Surface.subsurface(GRASS, (GAME_ZONE.left,
                                                          GAME_ZONE.top,
                                                          TEXTURE_SIZE,
                                                          TEXTURE_SIZE))
        for line in range(GAME_ZONE.left, GAME_ZONE.right, TEXTURE_SIZE):
            for column in range(GAME_ZONE.top, GAME_ZONE.bottom, TEXTURE_SIZE):
                pygame.Surface.blit(SCREEN, textured_mash, (line, column))
        events(Mirosha)
        Mirosha.update_person()
        Mirosha.output()

        clock.tick(FPS)
        pygame.display.update() # SCREEN update
        pass

main()

