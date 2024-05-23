import numpy as np
from scipy.signal import convolve2d
from skimage.color import rgb2gray
from skimage.util import img_as_float


def emboss_filter(images, kernel_size):
    emboss_images = []

    for image in images:
        if len(image.shape) == 3:
            image = rgb2gray(image)

        image_float = img_as_float(image)

        # Definir el kernel para emboss
        kernel = _create_emboss_kernel(kernel_size)

        # Aplicar convolución 2D con el kernel
        emboss_image = convolve2d(image_float, kernel, mode='same', boundary='symm')

        emboss_images.append(emboss_image)

    return emboss_images


def _create_emboss_kernel(size):
    half_size = size // 2
    kernel = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            if i == half_size and j == half_size:
                kernel[i][j] = 1
            elif i == 0 or j == 0 or i == size - 1 or j == size - 1:
                kernel[i][j] = 0
            else:
                kernel[i][j] = -1
    return kernel