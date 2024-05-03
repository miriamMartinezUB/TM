from PIL import Image
import numpy as np


def binarization_filter(images, threshold=70):
    binarized_images = []
    for image in images:
        # Convert image to grayscale
        gray_image = image.convert('L')

        # Convert PIL image to numpy array
        image_np = np.array(gray_image)

        # Apply threshold to create binary image
        binary_image_np = np.where(image_np > threshold, 255, 0).astype(np.uint8)

        # Convert back to PIL image
        binary_image = Image.fromarray(binary_image_np)
        binarized_images.append(binary_image)
    return binarized_images