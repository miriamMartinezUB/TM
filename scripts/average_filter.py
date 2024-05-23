from skimage.color import rgb2gray
from skimage.filters import rank
from skimage.morphology import disk
from skimage.util import img_as_ubyte, img_as_float


def average_filter(images, kernel_size):
    avg_images = []

    for image in images:
        if len(image.shape) == 3:
            image = rgb2gray(image)

        image_ubyte = img_as_ubyte(image)

        selem = disk(kernel_size)
        filtered_img = rank.mean(image_ubyte, footprint=selem)

        filtered_img_float = img_as_float(filtered_img)
        avg_images.append(filtered_img_float)

    return avg_images