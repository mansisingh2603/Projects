import os
import random
import game_config as gc
from pygame import image, transform

animal_count = dict((a, 0) for a in gc.ASSET_FILES)       


def available_animals():
    return [a for a, c in animal_count.items() if c < 2]


class Animal:
    def __init__(self, index):
        self.index = index
        self.name = random.choice(available_animals())
        self.image_path = os.path.join(gc.ASSET_DIR, self.name)  # loading pictures of animals
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        self.skip = False  # a flag. if a pair of animals match then we can skip printing the image of that animal
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))
        # blank white picture shown on screen
        self.box = self.image.copy()
        self.box.fill((200, 200, 200))  # 200,200,200 are the RGB values of the blank image

        animal_count[self.name] += 1
