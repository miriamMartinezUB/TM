import numpy as np
from scipy.signal import convolve2d
from skimage.color import rgb2gray
from skimage.util import img_as_float


def sharpen_filter(images):
    sharpened_images = []

    for image in images:
        if len(image.shape) == 3:
            image = rgb2gray(image)

        image_float = img_as_float(image)

        # Definir el kernel para el filtro de sharpen
        kernel = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])

        # Aplicar convolución 2D con el kernel
        sharpened_image = convolve2d(image_float, kernel, mode='same', boundary='symm')

        # Asegurar que los valores estén en el rango válido (entre 0 y 1)
        sharpened_image = np.clip(sharpened_image, 0, 1)

        sharpened_images.append(sharpened_image)

    return sharpened_images