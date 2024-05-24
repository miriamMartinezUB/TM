import skimage
from skimage.color import rgb2gray, gray2rgb
from skimage.util import img_as_float


def sobel_filter(images):
    """
    Aplica el filtre de Sobel a una llista d'imatges.

    Args:
        images (list): Llista d'imatges (cada imatge és un array de numpy).

    Returns:
        list: Llista d'imatges amb el filtre de Sobel aplicat com arrays de numpy.
    """
    sobel_images = []
    for img in images:
        # Convertir a RGB si la imagen está en escala de grises
        if len(img.shape) == 2:  # Es una imagen en escala de grises
            img = gray2rgb(img)
        img_f = rgb2gray(img_as_float(img))
        sobel_img = skimage.filters.sobel(image=img_f)
        sobel_images.append(sobel_img)
    return sobel_images