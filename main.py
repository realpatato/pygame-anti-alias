''' IMPORTS '''
#needed for visuals
import pygame

''' PYGAME SETUP '''
pygame.init()

screen_width = 401
screen_height = 301
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("anti-aliasing testing")

''' GAME LOOP SETUP '''
clock = pygame.time.Clock()
keep_playing = True

while keep_playing:
    for event in pygame.event.get():
        #check if the player has quit
        if event.type == pygame.QUIT:
            #set control variable to false
            keep_playing = False
    
    screen.fill((0, 0, 0))
    #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(51, 51, 1, 1))

    #update the screen
    pygame.display.update()

    #ticks the clock
    clock.tick(60)

''' ENDING THE PROGRAM '''
#quits the window
pygame.quit()
#ends the program
quit()