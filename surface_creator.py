''' SURFACE_CREATOR.PY - Used to create the surfaces that the module outputs '''
''' IMPORTS '''
import numpy as np
import pygame as pg

def create_surf_array(width, height):
    ''' Function used to create the a surface array which will store the shape. '''
    #creates an array full of small lists representing pixels
    #the pixels store rgba values
    surf_array = np.zeros((width, height, 4), dtype=np.uint8)
    #returns the array
    return surf_array

def change_pixel(surf_array, x, y, color):
    ''' Function used to modify a pixel at a given coordinate '''
    #tries so that index errors are caught, specifically for going off-screen
    try:
        #checks if x and y are negative
        if x < 0 or y < 0:
            #raises index error (prevents wrapping)
            raise IndexError
        #tries so that index errors for color are caught
        try:
            #changes the pixel at the coordinate
            surf_array[x][y] = [color[0], color[1], color[2], color[3]]
        #excepts index errors for colors without "a" value
        except IndexError:
            #changes the pixel at the coordinate
            surf_array[x][y] = [color[0], color[1], color[2], 255]
    #excepts index errors for situations where position is invalid
    except IndexError:
        #pass since nothing has to be done
        pass

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