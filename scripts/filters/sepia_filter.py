import numpy as np
from skimage.util import img_as_float


def sepia_filter(images):
    """
    Aplica un filtre sépia a una llista d'imatges.

    Args:
        images (list): Llista d'imatges (cada imatge és un array de numpy).

    Returns:
        list: Llista d'imatges sépia com arrays de numpy.
    """
    sepia_images = []

    # Coeficientes para la transformación de color sepia
    sepia_matrix = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])

    for image in images:
        # Convertir la imagen a flotante si no lo está
        image_float = img_as_float(image)

        # Aplicar la transformación sepia a cada píxel
        sepia_image = np.dot(image_float, sepia_matrix.T)

        # Asegurar que los valores estén en el rango válido (entre 0 y 1)
        sepia_image = np.clip(sepia_image, 0, 1)

        sepia_images.append(sepia_image)

    return sepia_images