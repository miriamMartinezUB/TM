import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image


def show_images_as_video(image_path,fps):

    fig = plt.figure()

    ims = []
    for image in image_path:
        img = Image.open(image)
        ims.append([plt.imshow(img, animated=True)])
    interval = 1000 / fps
    ani = animation.ArtistAnimation(fig, ims, interval=interval, blit=True, repeat_delay=0)
    plt.axis('off')
    plt.show()