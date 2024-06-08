import pygame

displayWidth = 1000
displayHeight = 800
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
lavender = (230, 230, 250)

crashed = False
gameDisplay.fill(lavender)

#game loop
while not crashed:
    for event in pygame.event.get():
        #if user quits the window (close it)
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                crashed = True

            if event.key == pygame.K_UP:
                print("Up is clicked")
            if event.key == pygame.K_RIGHT:
                print("Right is clicked")
            if event.key == pygame.K_LEFT:
                print("Left is clicked")
            if event.key == pygame.K_DOWN:
                print("Down is clicked")
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("the mouse was clicked")
            print(pygame.mouse.get_pos()) #xy if only want one value use index pygame.mouse.get_pos()(0) after gets x

        gameDisplay.fill(lavender)
        pygame.display.update()