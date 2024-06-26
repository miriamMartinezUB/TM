import matplotlib.animation as animation
import matplotlib.pyplot as plt
from tqdm import tqdm


def show_images_as_video(image_path, fps, cmap):
    """
    Reprodueix un vídeo a partir d'una seqüència d'imatges amb el nombre de quadres especificat.

    Args:
        image_path (list): Ruta on es troben els fotogrames.
        fps (int): Nombre de fotogrames per segon per mostrar el vídeo.
        cmap (str): Mapa de colors utilitzat per mostrar les imatges. Estableix 'gray' per a imatges en escala de grisos.

    Returns:
        None
    """
    fig, ax = plt.subplots()

    if cmap == 'gray':
        image_display = ax.imshow(image_path[0], cmap='gray')
    else:
        image_display = ax.imshow(image_path[0])

    interval = 1000 / fps
    progress_bar = tqdm(total=len(image_path), desc="Processing frames", unit="frame")

    def update(frame):
        image_display.set_array(image_path[frame])
        progress_bar.update(1)
        if frame == len(image_path) - 1:
            progress_bar.reset()

    ani = animation.FuncAnimation(fig, update, frames=len(image_path), interval=interval, repeat=True)
    plt.axis('off')
    plt.show()
    progress_bar.close()