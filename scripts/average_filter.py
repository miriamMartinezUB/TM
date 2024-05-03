import numpy as np
import matplotlib.pyplot as plt
from skimage import io, util
from scipy.ndimage import convolve

def average_filter(images , kernel_size=3):
    avg_images = []
    # Create the kernel for averaging
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)

    for image in images:
    # Apply the convolution
        avg_images.append(convolve(image, kernel))

    return avg_images