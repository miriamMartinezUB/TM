import numpy as np
from scipy.signal import convolve2d
from skimage.color import rgb2gray
from skimage.util import img_as_float


def average_filter(images):
    avg_images = []

    # Definir el kernel
    kernel = 1 / 9 * np.array([[1, 1, 1],
                               [1, 1, 1],
                               [1, 1, 1]])

    for image in images:
        if len(image.shape) == 3:
            image = rgb2gray(image)

        image_float = img_as_float(image)

        # Aplicar la convolución 2D con el kernel
        filtered_img = convolve2d(image_float, kernel, mode='same', boundary='symm')

        avg_images.append(filtered_img)

    return avg_images