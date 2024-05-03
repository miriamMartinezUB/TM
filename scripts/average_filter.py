import numpy as np
import skimage
from skimage.morphology import disk


def average_filter(images, kernel_size):
    avg_images = []

    for image in images:
        filtered_img = skimage.filters.rank.mean(image, disk(kernel_size[0],kernel_size[1]))
        avg_images.append(filtered_img)

    return avg_images