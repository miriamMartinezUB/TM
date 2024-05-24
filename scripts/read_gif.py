from PIL import Image

def extract_frames_from_gif(gif_path):
    '''
    This method extracts frames from a GIF file.
    :param gif_path: path where the GIF is located
    :return : frames, as a list of frames that gif file contains
    '''
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

# Opcional: guardar los frames como archivos separados para verificar
#for i, frame in enumerate(frames):
#    frame.save(f'frame_{i}.png')
