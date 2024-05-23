import numpy as np
from scipy.signal import convolve2d
from skimage.color import rgb2gray
from skimage.util import img_as_float


def emboss_filter(images):
    emboss_images = []

    for image in images:
        if len(image.shape) == 3:
            image = rgb2gray(image)

        image_float = img_as_float(image)

        # Definir el kernel para emboss
        kernel = np.array([[-2, -1, 0],
                           [-1, 1, 1],
                           [0, 1, 2]])

        # Aplicar convolución 2D con el kernel
        emboss_image = convolve2d(image_float, kernel, mode='same', boundary='symm')

        emboss_images.append(emboss_image)

    return emboss_images