''' DRAW.PY HANDLES DRAWING '''
''' IMPORTS '''
import surface_creator as sc

def rect(surface, color, rect, border_width=0):
    ''' Draws a rect! '''
    #creates a surface
    surf_array = sc.create_surf_array(surface.get_width(), surface.get_height())
    #checks if the width of the border is 0 or not
    if border_width == 0:
        #draws it
        for i in range(rect[2]):
            for k in range(rect[3]):
                surf_array[i + rect[0]][k + rect[1]] = [color[0], color[1], color[2], 255]
    #converts the array to a surface
    output_surface = sc.create_surface(surf_array)
    #outputs the surface
    surface.blit(output_surface, (0, 0))