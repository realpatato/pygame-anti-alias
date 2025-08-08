''' SURFACE_CREATOR.PY - Used to create the surfaces that the module outputs '''
''' IMPORTS '''
import numpy as np
import pygame as pg

def create_surf_array(width, height):
    ''' Function used to create the a surface array which will store the shape. '''
    #creates an array full of small lists representing pixels
    #the pixels store rgba values
    surf_array = np.zeros((width, height, 4), dtype=np.uint8)
    for i in range(10):
        for k in range(10):
            surf_array[i + 100][k + 20] = [255, 0, 0, 255]
    #returns the array
    return surf_array

def create_surface(surf_array):
    ''' Function which converts a surf array to a surface '''
    #creates a copy of the surfarray, but the height and width are swapped
    surf_swapped = surf_array.swapaxes(0, 1).copy()
    #gets the height and width of the surf array
    height, width = surf_swapped.shape[:2]
    #creates the surface, converts array to bytes, uses its size, and uses rgba, converting to alpha to have the a shown
    surface = pg.image.frombuffer(surf_swapped.tobytes(), (width, height), "RGBA").convert_alpha()
    #returns newly created surface
    return surface