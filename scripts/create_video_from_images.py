import cv2


def video_from_images(images, fps, file_name):
    """
    Crea un vídeo a partir d'una llista d'imatges.

    Args:
        images (list): Llista d'imatges (cada imatge és un array de numpy).
        fps (int): Fotogrames per segon per al vídeo.

    Returns:
        No retorna res, però genera un file de sortida que es diu video_salida.avi on es pot veure el vídeo amb els filtres que hàgim aplicat si és que ho hem fet.
    """
    height, width, _ = images[0].shape

    ruta_video = f'{file_name}.avi'
    codec = cv2.VideoWriter_fourcc(*'XVID')
    video_salida = cv2.VideoWriter(ruta_video, codec, float(fps), (width, height))

    for image in images:
        video_salida.write(image)

    video_salida.release()