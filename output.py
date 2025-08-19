''' OUTPUT.PY - Used for outputing created images/frames, for testing purposes '''
''' IMPORTS '''
#needed for outputting visual
import pygame
import draw

''' PYGAME SETUP '''
#initiates the pygame module
pygame.init()

#defines a width and height for the screen
screen_width = 500
screen_height = 500
#creates the screen
screen = pygame.display.set_mode((screen_width, screen_height))
#changes the caption of the screen
pygame.display.set_caption("anti-aliasing testing")

''' GAME LOOP SETUP '''
#clock for controlling frame rate
clock = pygame.time.Clock()
#variable for controlling game loop
keep_playing = True


''' GAME LOOP '''
while keep_playing:
    #iterates over each possible pygame event
    for event in pygame.event.get():
        #check if the player has quit
        if event.type == pygame.QUIT:
            #set control variable to false
            keep_playing = False
    
    screen.fill((0, 0, 0))

    draw.rect(screen, (255, 0, 0), (20, 20, 100, 50), 5)
    pygame.draw.rect(screen, (255, 0, 0), (20, 120, 100, 50), 5)

    '''
    Here is a list of tests that you can use. They each have pygame example with them, for comparison
    *** Basic Line Tests ***
    * Horizontal Lines *
    draw.line(screen, (255, 0, 0), (50, 150), (50, 250))
    draw.line(screen, (255, 0, 0), (52, 250), (52, 150))
    pygame.draw.line(screen, (255, 0, 0), (54, 250), (54, 150))

    * Vertical Lines *
    draw.line(screen, (255, 0, 0), (150, 50), (250, 50))
    draw.line(screen, (255, 0, 0), (250, 52), (150, 52))
    pygame.draw.line(screen, (255, 0, 0), (250, 54), (150, 54))

    *** Lines with Widths Tests ***
    * Horizontal Lines Even Width
    draw.line(screen, (255, 255, 255), (150, 50), (250, 50), 4)
    draw.line(screen, (255, 0, 0), (150, 50), (250, 50))
    pygame.draw.line(screen, (255, 255, 255), (250, 60), (150, 60), 4)
    pygame.draw.line(screen, (255, 0, 0), (250, 60), (150, 60))
    
    * Horizontal Lines Odd Width *
    draw.line(screen, (255, 255, 255), (150, 50), (250, 50), 5)
    draw.line(screen, (255, 0, 0), (150, 50), (250, 50))
    pygame.draw.line(screen, (255, 255, 255), (250, 60), (150, 60), 5)
    pygame.draw.line(screen, (255, 0, 0), (250, 60), (150, 60))
    
    * Vertical Lines Even Width *
    draw.line(screen, (255, 255, 255), (50, 150), (50, 250), 4)
    draw.line(screen, (255, 0, 0), (50, 150), (50, 250))
    pygame.draw.line(screen, (255, 255, 255), (60, 250), (60, 150), 4)
    pygame.draw.line(screen, (255, 0, 0), (60, 250), (60, 150))
    
    * Vertical Lines Odd Width *
    draw.line(screen, (255, 255, 255), (50, 150), (50, 250), 5)
    draw.line(screen, (255, 0, 0), (50, 150), (50, 250))
    pygame.draw.line(screen, (255, 255, 255), (60, 250), (60, 150), 5)
    pygame.draw.line(screen, (255, 0, 0), (60, 250), (60, 150))

    *** Basic Rect Tests ***
    * Filled Rect *
    draw.rect(screen, (255, 0, 0), (100, 20, 100, 50))
    pygame.draw.rect(screen, (255, 0, 0), (100, 20, 100, 50))
    '''

    #update the screen
    pygame.display.update()

    #ticks the clock
    clock.tick(60)

''' ENDING THE PROGRAM '''
#quits the window
pygame.quit()
#ends the program
quit()