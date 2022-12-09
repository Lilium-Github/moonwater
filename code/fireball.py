import pygame
from settings import *
from support import *
from timer import Timer

class Fireball(pygame.sprite.Sprite): #this is a child class of pygame's sprite class
    def __init__(self, pos, group,player):
        super().__init__(group) # gives the class access to the functions inside the Group class

        self.player = player

        self.import_all()
        self.status = 'base'
        self.frame_index = 0

        #general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS["fireball"]
      
        self.timers = {
            "shoot": Timer(500, self.explode),
            "explode": Timer(300, self.reset),
            "active": Timer(800)
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
        if self.timers["active"].active:
            self.pos += self.direction * self.speed * dt

        self.rect.center = self.pos

    def shoot(self):
        self.pos.x = self.player.pos.x
        self.pos.y = self.player.pos.y
        print("foo")
        self.timers["active"].activate()
        self.timers["shoot"].activate()
        
        p_status = self.player.status.split("_")[0]

        if p_status == "left":
            self.direction.x = self.direction.x = -1
        elif p_status == "right":
            self.direction.x = self.direction.x = 1
        elif p_status == "up":
            self.direction.y = self.direction.y = -1
        elif p_status == "down":
            self.direction.y = self.direction.y = 1

    def explode(self):
        self.direction.x = 0
        self.direction.y = 0

        print(self.pos)
        print(self.player.pos)

        self.timers["explode"].activate()

    def reset(self):
        self.pos.x = self.player.pos.x
        self.pos.y = self.player.pos.y

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update(self, dt):
        self.move(dt)
        self.animate(dt)
        self.update_timers()