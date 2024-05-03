import skimage

from skimage.color import rgb2gray
from skimage.util import img_as_float


def sobel_filter(images, kernel):
    sobel_images = []
    for img in images:
        img_f = rgb2gray(img_as_float(img))
        sobel_img = skimage.filters.sobel(image=img_f)
        sobel_images.append(sobel_img)
    return sobel_images