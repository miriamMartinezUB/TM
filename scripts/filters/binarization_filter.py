import numpy as np
from skimage.color import rgb2gray


def binarization_filter(images, threshold):
    binarized_images = []
    for image in images:
        # Convert image to grayscale
        gray_image = rgb2gray(image)
        gray_image = 255 * gray_image

        # Apply threshold to create binary image
        binary_image_np = np.where(gray_image > int(threshold), 255, 0).astype(np.uint8)

        binarized_images.append(binary_image_np)
    return binarized_images