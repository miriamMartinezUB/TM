import os
import cv2
import numpy as np
from skimage.measure import block_reduce


def extract_frames(video_path):
    frames = []
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames


def compare_tiles_dct(tile1, tile2, threshold=0.1):
    # Aplicar DCT a las teselas
    dct1 = cv2.dct(tile1.astype(np.float32))
    dct2 = cv2.dct(tile2.astype(np.float32))

    # Normalizar las DCTs
    dct1 /= np.sqrt(tile1.shape[0] * tile1.shape[1])
    dct2 /= np.sqrt(tile2.shape[0] * tile2.shape[1])

    # Comparar las DCTs
    diff = np.sum(np.abs(dct1 - dct2))
    return diff <= threshold


def encode_video(video_path, gop_size, tile_size, max_shift, output_dir):
    # Extrae los frames del vídeo
    frames = extract_frames(video_path)

    # Divide los frames en grupos basados en el GOP
    gop_frames = [frames[i:i + gop_size] for i in range(0, len(frames), gop_size)]

    # Itera sobre cada grupo de imágenes
    for i, group in enumerate(gop_frames):
        # La primera imagen del grupo es la imagen de referencia
        reference_frame = group[0]

        # Itera sobre las imágenes restantes en el grupo
        for j in range(1, len(group)):
            current_frame = group[j]

            # Subdivide la imagen en teselas
            reference_tiles = block_reduce(reference_frame, block_size=(tile_size, tile_size), func=np.mean)
            current_tiles = block_reduce(current_frame, block_size=(tile_size, tile_size), func=np.mean)

            # Itera sobre las teselas y compáralas con las de la imagen de referencia
            for x in range(reference_tiles.shape[0]):
                for y in range(reference_tiles.shape[1]):
                    tile1 = reference_tiles[x, y]
                    tile2 = current_tiles[x, y]

                    # Compara las teselas y marca las que son equivalentes para eliminación
                    if compare_tiles_dct(tile1, tile2):
                        current_frame[x * tile_size:(x + 1) * tile_size, y * tile_size:(y + 1) * tile_size] = np.mean(
                            current_frame)

        # Guarda el vídeo codificado en el directorio de salida especificado
        output_path = os.path.join(output_dir, f"encoded_group_{i}.avi")
        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), 30,
                              (frames[0].shape[1], frames[0].shape[0]))
        for frame in group:
            out.write(frame)
        out.release()


# Ejemplo de uso
video_path = "data/raw/sample.avi"
output_directory = "data/tmp"  # Directorio de salida especificado
encode_video(video_path, gop_size=10, tile_size=8, max_shift=5, output_dir=output_directory)