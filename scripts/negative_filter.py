from PIL import Image
from skimage import util
def negative_filter(images):
    negative_images = []
    for image in images:
        negative_images.append(util.invert(image))
    return negative_images
