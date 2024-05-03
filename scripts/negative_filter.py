from PIL import Image
import numpy as np

def negative_filter(images):
    negative_images = []
    for image in images:
        # Convert PIL image to numpy array
        image_np = np.array(image)
        # Invert the colors
        inverted_image_np = 255 - image_np
        # Convert back to PIL image
        inverted_image = Image.fromarray(inverted_image_np)
        negative_images.append(inverted_image)
    return negative_images