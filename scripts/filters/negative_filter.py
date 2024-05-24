def negative_filter(images):
    """
    Aplica un filtre negatiu a una llista d'imatges.

    Args:
        images (list): Llista d'imatges (cada imatge és un array de numpy).

    Returns:
        list: Llista d'imatges negatives com arrays de numpy.
    """
    negative_images = []
    for image in images:
        inverted_image_np = 255 - image
        negative_images.append(inverted_image_np)
    return negative_images