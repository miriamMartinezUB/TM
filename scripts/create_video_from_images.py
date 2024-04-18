import os

import cv2


def video_from_images(fps):
    directorio_imagenes = 'data/raw/Cubo'

    # Lista de nombres de archivo de las imágenes
    nombres_archivos = sorted(os.listdir(directorio_imagenes))


    # Determinar el tamaño de una imagen para configurar el tamaño del video
    imagen_ejemplo = cv2.imread(os.path.join(directorio_imagenes, nombres_archivos[0]))
    alto, ancho, _ = imagen_ejemplo.shape

    # Configurar el objeto VideoWriter
    ruta_video = 'video_salida.avi'  # Nombre del archivo de video de salida
    fps = 30  # Cuadros por segundo del video
    codec = cv2.VideoWriter_fourcc(*'XVID')  # Codec para el archivo de video (AVI)
    video_salida = cv2.VideoWriter(ruta_video, codec, fps, (ancho, alto))

    # Iterar sobre las imágenes y agregarlas al video
    for nombre_archivo in nombres_archivos:
        ruta_imagen = os.path.join(directorio_imagenes, nombre_archivo)
    imagen = cv2.imread(ruta_imagen)
    video_salida.write(imagen)

    # Liberar el objeto VideoWriter
    video_salida.release()