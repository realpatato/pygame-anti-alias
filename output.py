''' OUTPUT.PY - Used for outputing created images/frames '''
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

for i in range(-100):
    print("Iterate")
    print(i)

''' GAME LOOP '''
while keep_playing:
    #iterates over each possible pygame event
    for event in pygame.event.get():
        #check if the player has quit
        if event.type == pygame.QUIT:
            #set control variable to false
            keep_playing = False
    
    screen.fill((0, 0, 0))

    #pygame.draw.line(screen, (255, 255, 255), (250, 150), (50, 150))
    
    #print(4//2)

    draw.line(screen, (255, 0, 0), (50, 150), (50, 250))
    draw.line(screen, (255, 0, 0), (52, 250), (52, 150))
    pygame.draw.line(screen, (255, 0, 0), (54, 250), (54, 150))

    draw.line(screen, (255, 0, 0), (150, 50), (250, 50))
    draw.line(screen, (255, 0, 0), (250, 52), (150, 52))
    pygame.draw.line(screen, (255, 0, 0), (250, 54), (150, 54))

    #draw.rect(screen, (255, 0, 0), (100, 20, 100, 50))

    #update the screen
    pygame.display.update()

    #ticks the clock
    clock.tick(60)

''' ENDING THE PROGRAM '''
#quits the window
pygame.quit()
#ends the program
quit()