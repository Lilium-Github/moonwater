import pygame
from settings import *
from support import *

class Water(pygame.sprite.Sprite): #this is a child class of pygame's sprite class
    def __init__(self, pos, group):
        super().__init__(group) # gives the class access to the functions inside the Group class

        self.import_all()
        self.status = 'base'
        self.frame_index = 0

        #general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS["water"]

        self.pos = pygame.math.Vector2(self.rect.center)


    def import_all(self):
        self.animations = {'base':[]}

        for animation in self.animations.keys():
            full_path = 'moonwater/graphics/water/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self,dt):
        self.frame_index += dt

        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def update(self, dt):
        self.animate(dt)
        
