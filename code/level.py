import pygame
from settings import * 
from player import Player
from fireball import Fireball
from overlay import Overlay
from sprites import Generic

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = CamGroup()

        self.setup()

    def setup(self):
        Generic(
            pos = (0,0),
            surf = pygame.image.load("moonwater/graphics/ground.png").convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS["ground"]
        )

        self.sounds = {
            "explode": pygame.mixer.Sound('moonwater/sounds/explode.wav'),
            "menu": pygame.mixer.Sound('moonwater/sounds/menu.wav'),
            "shoot": pygame.mixer.Sound('moonwater/sounds/shoot.wav'),
            "axe": pygame.mixer.Sound('moonwater/sounds/axe.wav')
        }

        self.player = Player((640,360), self.sounds, self.all_sprites)
        self.player.fireball = Fireball((640,360), self.all_sprites, self.player)
        self.overlay = Overlay(self.player)


    def run(self, dt):
        #print("run, forrest, run!")

        self.display_surface.fill('black')
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)
        self.overlay.display()
       
class CamGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2
        for layer in LAYERS.values():    
            for sprite in self.sprites():
                if sprite.z == layer: 
                    if layer != LAYERS["fireball"] or sprite.timers["active"].active:
                        offset_rect = sprite.rect.copy()
                        offset_rect.center -= self.offset
                        self.display_surface.blit(sprite.image, offset_rect)
