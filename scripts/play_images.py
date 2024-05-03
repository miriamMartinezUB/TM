import matplotlib.animation as animation
import matplotlib.pyplot as plt


def show_images_as_video(image_path, fps, cmap):
    fig = plt.figure()

    ims = []
    for image in image_path:
        ims.append([plt.imshow(image, animated=True)])
    interval = 1000 / fps
    ani = animation.ArtistAnimation(fig, ims, interval=interval, blit=True, repeat_delay=0)
    plt.axis('off')
    if cmap == 'gray':
        plt.show(cmap='gray')
    else:
        plt.show()