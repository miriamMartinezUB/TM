import numpy as np
from scipy.signal import convolve2d
from skimage.color import rgb2gray
from skimage.util import img_as_float


def blur_filter(images):
    blur_images = []

    # Definir el kernel
    kernel = np.array([[0, 0.2, 0],
                       [0.2, 0.2, 0.2],
                       [0, 0.2, 0]])

    for image in images:
        if len(image.shape) == 3:
            image = rgb2gray(image)

        image_float = img_as_float(image)

        # Aplicar la convolución 2D con el kernel
        filtered_img = convolve2d(image_float, kernel, mode='same', boundary='symm')

        blur_images.append(filtered_img)

    return blur_images