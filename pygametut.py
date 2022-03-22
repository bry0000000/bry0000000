"""
Tutorial from https://www.youtube.com/watch?v=i6xMBig-pP4
"""

from pickle import TRUE
import pygame
pygame.init()

win = pygame.display.set_mode((500,500)) #create a window, put it in a var to keep it easy to call

pygame.display.set_caption("Bryan's First Window")

x = 50 # starting x coordinate
y = 425 # starting y coordinate
width  = 40 # width of character
height = 60 # height of character
vel = 5 #controls speed of character movement

run = True

isJump = False #detects if we've engaged a jump
jumpCount = 10



""" all games in pygame have a main loop. THis is what checks the key inputs
if the game has ended, collision, etc.

"""

while run:  ## main python loop
    pygame.time.delay(100) #delay measured in miliseconds
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run= False
    
    pygame.draw.rect(win, (0,255,0), (x, y, width, height))
    pygame.display.update() # refreshes the screen with all prev commands. Character won't show up without it.

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -=vel
        # -= operator subtracts the value and appends it to the original variable

    if keys[pygame.K_RIGHT] and x < 460: #500 is width of screen, character is 40, so this is 500 - width of character
        x+= vel

    if not(isJump): ## Ensure player can't move up or down while jumping

        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 440:
            y += vel
    

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >=-10 and y < 440:
            neg = 1 # Detects if jumpCount is a negative num, so we can tell jump to return to ground
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg #neg variable becomes positive, which moves down on y axis            jumpCount -= 1
            jumpCount = -1

        else:
            isJump = False
            jumpCount = 10

    


    
    win.fill((255,255,255))
    

pygame.quit()
         
