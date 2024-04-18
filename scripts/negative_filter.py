
import matplotlib.pyplot as plt
from skimage import io, util
def negative_filter(image_path):
    image = io.imread(image_path, as_gray=True)

    # Apply the negative filter
    negative_image = util.invert(image)

    # Display the original and negative images
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(negative_image, cmap='gray')
    plt.title('Negative Image')
    plt.axis('off')

    plt.show()
