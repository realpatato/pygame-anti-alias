''' DRAW.PY HANDLES DRAWING '''
''' IMPORTS '''
import surface_creator as sc

def line(surface, color, start_pos, end_pos, width: int=1):
    ''' Draws a line! '''
    #determines if a line can be drawn
    if width >= 0:
        #create the surface
        surf_array = sc.create_surf_array(surface.get_width(), surface.get_height())
        #handle width
        width_begin = -1 * ((width - 1) // 2)
        #determines if the line is straight and if it is vertical or horizontal
        if start_pos[0] == end_pos[0]:
            #iterates over each line in the width
            for w in range(width):
                #iterates over each pixel
                for i in range(abs(start_pos[1] - end_pos[1]) + 1):
                    #checks if start pos is greater than end
                    if start_pos[1] > end_pos[1]:
                        sc.change_pixel(surf_array, start_pos[0] + width_begin, i + end_pos[1], color)
                    else:
                        sc.change_pixel(surf_array, start_pos[0] + width_begin, i + start_pos[1], color)
                #shifts width begin over by one
                width_begin += 1
        elif start_pos[1] == end_pos[1]:
            #iterates over each line in the width
            for w in range(width):
                #iterates over each pixel
                for i in range(abs(start_pos[0] - end_pos[0]) + 1):
                    #checks if start pos is greater than end
                    if start_pos[0] > end_pos[0]:
                        sc.change_pixel(surf_array, i + end_pos[0], start_pos[1] + width_begin, color)
                    else:
                        sc.change_pixel(surf_array, i + start_pos[0], start_pos[1] + width_begin, color)
                #shifts width begin over by one
                width_begin += 1
        #converts the array to a surface
        output_surface = sc.create_surface(surf_array)
        #outputs the surface
        surface.blit(output_surface, (0, 0))

def rect(surface, color, rect, width: int=0):
    ''' Draws a rect! '''
    #creates a surface
    surf_array = sc.create_surf_array(surface.get_width(), surface.get_height())
    #checks if the width of the border is 0 or not
    if width == 0:
        #draws it
        for i in range(rect[2]):
            for k in range(rect[3]):
                sc.change_pixel(surf_array, i + rect[0], k + rect[1], color)
    else:
        #get the max width
        #this prevents the outline from overflowing
        if rect[2] > rect[3]:
            #plus one to compensate for rects with odd number widths
            max_width = (rect[3] // 2) + 1
        else:
            #plus one to compensate for rects with odd number widths
            max_width = (rect[2] // 2) + 1
        #sets the width to the max width if the width is too much
        if width > max_width:
            width = max_width
            #draws the rect as an outline
        for i in range(width):
            line(surface, color, (rect[0], rect[1] + i), (rect[0] + rect[2], rect[1] + i))
            line(surface, color, (rect[0], (rect[1] + rect[3]) - i), (rect[0] + rect[2], (rect[1] + rect[3]) - i))
            line(surface, color, (rect[0] + i, rect[1]), (rect[0] + i, rect[1] + rect[3]))
            line(surface, color, ((rect[0] + rect[2]) - i, rect[1]), ((rect[0] + rect[2]) - i, rect[1] + rect[3]))
    #converts the array to a surface
    output_surface = sc.create_surface(surf_array)
    #outputs the surface
    surface.blit(output_surface, (0, 0))