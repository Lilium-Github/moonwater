import pygame
from settings import *
from support import *
from timer import Timer

class Fireball(pygame.sprite.Sprite): #this is a child class of pygame's sprite class
    def __init__(self, pos, group):
        super().__init__(group) # gives the Player class access to the functions inside the Group class

        self.import_all()
        self.status = 'base'
        self.frame_index = 0

        #general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS["main"]
      
        self.timers = {
            "shoot": Timer(500, self.explode),
            "explode": Timer(300, self.hide)
        }

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 500


    def import_all(self):
        self.animations = {'base':[], 'explode':[]}

        for animation in self.animations.keys():
            full_path = 'moonwater/graphics/fireball/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self,dt):
        self.frame_index += 5*dt

        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def move(self,dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def shoot(self, player):
        print("pew pew pew")
        self.timers["shoot"].activate()
        self.direction = player.direction


    def explode(self):
        self.direction.x = 0
        self.direction.y = 0

        self.timers["explode"].activate

    def hide(self):
        self.z = LAYERS["dont_draw"]

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update(self, dt):
        self.move(dt)
        self.animate(dt)
        self.update_timers()