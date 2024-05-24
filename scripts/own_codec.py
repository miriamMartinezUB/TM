import numpy as np
import cv2
from scipy.fftpack import dct
from tqdm import tqdm

def split_into_tiles(image, num_tiles):
    """
    Split an image into a given number of tiles.
    """
    height, width = image.shape[:2]
    tile_height = height // num_tiles
    tile_width = width // num_tiles
    tiles = []

    for i in range(num_tiles):
        for j in range(num_tiles):
            tile = image[i*tile_height:(i+1)*tile_height, j*tile_width:(j+1)*tile_width]
            tiles.append(tile)

    return tiles

def calculate_dct(tile):
    """
    Calculate the DCT of a tile.
    """
    return dct(dct(tile.T, norm='ortho').T, norm='ortho')

def calculate_correlation(tile1, tile2):
    """
    Calculate the correlation between two tiles using their DCT.
    """
    dct1 = calculate_dct(tile1)
    dct2 = calculate_dct(tile2)
    return np.corrcoef(dct1.flatten(), dct2.flatten())[0, 1]

def process_video(video, gop, num_tiles, max_displacement):
    """
    Process a video with the given parameters.
    """
    processed_video = []
    reference_frame = None

    for frame_idx in tqdm(range(len(video)), desc="Processing frames", unit="frame"):
        current_frame = video[frame_idx]

        if frame_idx % gop == 0:
            # Si es una imagen de referencia, añadirla sin modificar
            processed_video.append(current_frame)
            reference_frame = current_frame
            continue

        if reference_frame is None:
            reference_frame = current_frame

        current_tiles = split_into_tiles(current_frame, num_tiles)
        reference_tiles = split_into_tiles(reference_frame, num_tiles)

        new_frame = current_frame.copy()
        tile_height, tile_width = current_tiles[0].shape[:2]

        for idx, current_tile in enumerate(current_tiles):
            i = idx // num_tiles
            j = idx % num_tiles

            max_corr = -1
            best_tile = None

            for di in range(-max_displacement, max_displacement + 1):
                for dj in range(-max_displacement, max_displacement + 1):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < num_tiles and 0 <= nj < num_tiles:
                        ref_tile = reference_tiles[ni * num_tiles + nj]
                        corr = calculate_correlation(current_tile, ref_tile)
                        if corr > max_corr:
                            max_corr = corr
                            best_tile = ref_tile

            if max_corr > 0.95:  # Threshold for similarity
                new_frame[i*tile_height:(i+1)*tile_height, j*tile_width:(j+1)*tile_width] = np.mean(current_frame)

        processed_video.append(new_frame)

    return processed_video

