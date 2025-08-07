''' OUTPUT.PY - Used for outputing created images/frames '''
''' IMPORTS '''
#needed for outputting visual
import pygame

''' PYGAME SETUP '''
#initiates the pygame module
pygame.init()

#defines a width and height for the screen
screen_width = 401
screen_height = 301
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

    # Regular jaggy line
    pygame.draw.line(screen, (255, 255, 255), (50, 50), (350, 250), 1)

    # Anti-aliased line
    pygame.draw.aaline(screen, (255, 255, 255), (50, 70), (350, 270))

    #update the screen
    pygame.display.update()

    #ticks the clock
    clock.tick(60)

''' ENDING THE PROGRAM '''
#quits the window
pygame.quit()
#ends the program
quit()