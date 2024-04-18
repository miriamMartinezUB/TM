import numpy as np
import matplotlib.pyplot as plt
from skimage import io, util
from scipy.ndimage import convolve

def average_filter(image_path, kernel_size):
    # Read the image
    image = io.imread(image_path, as_gray=True)

    # Create the kernel for averaging
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)

    # Apply the convolution
    filtered_image = convolve(image, kernel)

    # Display the original and filtered images
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap='gray')
    plt.title(f'Averaging Filter (Kernel Size: {kernel_size})')
    plt.axis('off')

    plt.show()

