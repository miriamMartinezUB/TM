from skimage.color import rgb2gray


def grayscale_filter(images):
    """
    Aplica un filtre d'escala de grisos a una llista d'imatges.

    Args:
        images (list): Llista d'imatges (cada imatge és un array de numpy).

    Returns:
        list: Llista d'imatges en escala de grisos com arrays de numpy.
    """
    grayscale_images = []
    for image in images:
        grayscale_images.append(rgb2gray(image))
    return grayscale_images