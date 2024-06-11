import numpy as np
from tqdm import tqdm

from scripts.utils import calculate_correlation, split_into_tiles

def process_video(video, gop, num_tiles, max_displacement, quality):
    """
    Processa un vídeo amb els paràmetres donats.

    :param video: Vídeo d'entrada com una llista de fotogrames.
    :type video: list[numpy.ndarray]
    :param gop: Mida del grup d'imatges (GOP).
    :type gop: int
    :param num_tiles: Nombre de tessel·les en cada dimensió.
    :type num_tiles: int
    :param max_displacement: Desplaçament màxim per cercar correlacions.
    :type max_displacement: int
    :param quality: Qualitat mínima de la correlació per considerar una tessel·la.
    :type quality: float
    :return: Una tupla amb el vídeo processat i la informació dels fotogrames.
    :rtype: tuple(list[numpy.ndarray], list[dict])
"""
    processed_video = []
    reference_frame = []
    frames_info = []

    for frame_idx in tqdm(range(len(video)), desc="Processing frames", unit="frame"):
        current_frame = video[frame_idx]

        if frame_idx % gop == 0:
            # Si es una imagen de referencia, añadirla sin modificar
            processed_video.append(current_frame)
            reference_frame = current_frame
            frames_info.append({"frame_idx": frame_idx, "tiles_removed": []})

        else:
            current_tiles = split_into_tiles(current_frame, num_tiles)
            reference_tiles = split_into_tiles(reference_frame, num_tiles)

            mean_color = np.mean(current_frame, axis=(0, 1))

            new_frame = current_frame.copy()
            tile_height, tile_width = current_tiles[0].shape[:2]

            tiles_removed = []

            for idx, current_tile in enumerate(current_tiles):
                i = idx // num_tiles
                j = idx % num_tiles

                max_corr = -1
                best_tile = None
                best_tile_indices = (i, j)

                for di in range(-max_displacement, max_displacement + 1):
                    for dj in range(-max_displacement, max_displacement + 1):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < num_tiles and 0 <= nj < num_tiles:
                            ref_tile = reference_tiles[ni * num_tiles + nj]
                            corr = calculate_correlation(current_tile, ref_tile)
                            if corr > max_corr:
                                max_corr = corr
                                best_tile = ref_tile
                                best_tile_indices = (ni, nj)

                if max_corr > quality:  # Umbral para la similitud
                    new_frame[i * tile_height:(i + 1) * tile_height, j * tile_width:(j + 1) * tile_width] = mean_color
                    tiles_removed.append({
                        "current_tile_indices": (i, j),
                        "best_tile_indices": best_tile_indices
                    })

            processed_video.append(new_frame)
            frames_info.append({"frame_idx": frame_idx, "tiles_removed": tiles_removed})

    return processed_video, frames_info
