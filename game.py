import pygame
from animals import Animal
import game_config as gc
from pygame import display, event, image, mouse
from time import sleep


def find_index(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index


pygame.init()

display.set_caption('MY GAME')  # NAME OF THE GAME
screen = display.set_mode((512, 512))  # SCREEN DIMENSIONS
matched = image.load('otherassests/matched.png')  # DISPLAYING IMAGE ON SCREEN
win = image.load('otherassests/done.png')

# SETTING ITS PARAMETERS,
# (0,0) ENSURES THAT IT COVERS THE WHOLE SCREE
running = True

tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
current_images = []

while running:
    current_events = event.get()

    for e in current_events:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:  # close the window or press esc to close the game
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x, mouse_y)
            if index not in current_images:                         #checking for unique indices within current_images
                if len(current_images) > 1:
                    current_images = current_images[1:] + [index]   # it holds the second ele, ignores first
                else:
                    current_images.append(index)

    screen.fill((255, 255, 255))  # white background
    total_skipped = 0

    for i, tile in enumerate(tiles):            # to get index we use enumerate
        image_i = tile.image if i in current_images else tile.box
        if not tile.skip:
            screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN,     # display the images of animals in tiles on the screen using a loop and specifying the
                                 tile.row * gc.IMAGE_SIZE + gc.MARGIN))      # coordinates of the IMAGE size using the info in animals.py
        else:
            total_skipped += 1
    display.flip()

    if len(current_images) == 2:                                     # for exactly 2 indices in current_images
        idx1, idx2 = current_images                                  # two variables idx1,idx2 are given the values of current_images
        if tiles[idx1].name == tiles[idx2].name:                    # if names of index1=name of index 2
            tiles[idx1].skip = True                                # skip display of that image at given indices
            tiles[idx2].skip = True
            # display matched image
            sleep(0.4)
            screen.blit(matched,(0,0))
            display.flip()
            sleep(0.5)
            current_images = []

    if total_skipped == len(tiles):
        screen.blit(win , (0,0))
        display.flip()
        sleep(0.7)
        running = False

print('Goodbye!')
