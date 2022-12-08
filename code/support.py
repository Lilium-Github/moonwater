from os import walk 
import pygame

def import_folder(path):
    surface_list = []

    for _,_, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image #get the full path for each image
            image_surf = pygame.image.load(full_path).convert_alpha() #create pygame surface
            surface_list.append(image_surf)

    return surface_list