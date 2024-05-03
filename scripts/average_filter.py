import numpy as np
import skimage


def average_filter(images, kernel_size=3):
    avg_images = []

    for image in images:
        filtered_img = skimage.filters.rank.mean(image, selem=np.ones(kernel_size))
        avg_images.append(filtered_img)

    return avg_images