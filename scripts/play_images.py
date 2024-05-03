import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image


def show_images_as_video(image_path):

    fig = plt.figure()

    ims = []
    for image in image_path:
        img = Image.open(image)
        ims.append([plt.imshow(img, animated=True)])

    ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True, repeat_delay=1)
    plt.axis('off')
    plt.show()