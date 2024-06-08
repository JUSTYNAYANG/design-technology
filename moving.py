import pygame

white = (255,255,255)
beige = (222, 221, 216)

crashed=False


# image to a variable as you see here below.
chibi = pygame.image.load('images/luca.jpeg')

#Here we set up the size of the screen as a "tuple"
display_width = 800
display_height = 600
#gameDisplay is the window that open that displays graphics
#of course you can use any variable name here.
gameDisplay = pygame.display.set_mode((display_width,display_height))
#This is used for frame rate controls used in animation.
#It keeps track of passing time.
clock = pygame.time.Clock()
#starting x and y position of our alien
x=30
y=0


def appleDisplay(x,y):

    gameDisplay.blit(chibi, (x,y))



count=60
#How many pixels the alien moves with animation
move=10
right=False

start_ticks=pygame.time.get_ticks() #starter tick
while not crashed:
    #TIMER THIS WILL BE USED FOR ANIMATION
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    #Handles character movement
    if(int(seconds)%1==0):
        if right==True:
            if x<700:
                x+=move
            else:
                x -= move
                move=move*-1
            if x<30:
                x+=20
                move=move*-1
        else:
            if y<500:
                y+=move
            else:
                y -= move
                move=move*-1
            if y<30:
                y+=20
                move=move*-1

    for event in pygame.event.get():
        # This event handles clicking X on your window to quit program
        if event.type == pygame.QUIT:
            crashed = True
        # This event handles mouse clicks check position and checks for collision detection.
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            print(mousex, mousey)

        #Keyboard movement!
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move=10
                right=True
            if event.key == pygame.K_LEFT:
                move=-10
                right=True
            if event.key == pygame.K_UP:
                move=-10
                right=False
            if event.key == pygame.K_DOWN:
                move=10
                right=False
            if event.key == pygame.K_q:
                done = True
    #BG Color of your screen. This uses the variable name "white" set-up at the top of the code.
    gameDisplay.fill(beige)
    #This method "blits" AKA displays the graphic each time through the loop
    appleDisplay(x, y)
    #updates the screen graphics to account for movement on screen
    pygame.display.update()
    clock.tick(40)