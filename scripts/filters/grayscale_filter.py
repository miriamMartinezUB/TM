from skimage.color import rgb2gray


def grayscale_filter(images):
    grayscale_images = []
    for image in images:
        grayscale_images.append(rgb2gray(image))
    return grayscale_images