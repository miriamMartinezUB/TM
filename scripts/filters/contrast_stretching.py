import numpy as np
from skimage import exposure


def contrast_stretching(images):
    """
    Aplica l'estirament de contrast a una llista d'imatges.

    Args:
        images (list): Llista d'imatges (cada imatge és un array de numpy).

    Returns:
        list: Llista d'imatges amb el contrast estirat com arrays de numpy.
    """
    contrast_stretching_images = []
    for img in images:
        p2, p98 = np.percentile(img, (2, 98))
        img_contrast_stretched = exposure.rescale_intensity(img, in_range=(p2, p98))
        contrast_stretching_images.append(img_contrast_stretched)
    return contrast_stretching_images