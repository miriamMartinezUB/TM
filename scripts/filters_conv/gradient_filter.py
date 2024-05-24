import numpy as np
from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage.util import img_as_float


def gradient_filter(images):
    """
    Calcula el gradient de magnitud per a cada imatge en una llista.

    Args:
        images (list): Llista d'imatges (cada imatge és un array de numpy).

    Returns:
        list: Llista d'imatges amb el gradient de magnitud com arrays de numpy.
    """
    gradient_images = []

    for image in images:
        if len(image.shape) == 3:
            image = rgb2gray(image)

        image_float = img_as_float(image)

        gradient_x = sobel(image_float, axis=0)
        gradient_y = sobel(image_float, axis=1)

        gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)

        gradient_images.append(gradient_magnitude)

    return gradient_images