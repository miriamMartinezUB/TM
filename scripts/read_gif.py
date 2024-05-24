from PIL import Image


def extract_frames_from_gif(gif_path):
    """
    Extreu els fotogrames d'un fitxer GIF.

    :param gif_path: Ruta on es troba el fitxer GIF.
    :type gif_path: str
    :return: Fotogrames del fitxer GIF, com una llista d'imatges.
    :rtype: list
    """
    # Abrir el archivo gif
    gif = Image.open(gif_path)
    frames = []
    try:
        # Iterar sobre los frames del gif
        while True:
            # Copiar cada frame y añadirlo a la lista
            frame = gif.copy()
            frames.append(frame)
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass  # Fin del archivo gif
    return frames