from matplotlib.pyplot import imshow, show, subplot, title, axis
from skimage import io, util


def grayscale_filter(image_path):
    image = io.imread(image_path, as_gray=True)

    # Apply the negative filter
    negative_image = util.invert(image)

    # Display the original and negative images
    subplot(1, 2, 1)
    imshow(image, cmap='gray')
    title('Original Image')
    axis('off')

    subplot(1, 2, 2)
    imshow(negative_image, cmap='gray')
    title('Negative Image')
    axis('off')

    show()