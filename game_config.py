import os

IMAGE_SIZE = 128  # setting image size
SCREEN_SIZE = 512  # setting screen size
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 4
ASSET_DIR = 'assets'  # making a path to the assets folder
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']  # asset files will include all png files
assert len(ASSET_FILES) == 8  # ensuring that there are 8 images in the asset_files.
