import numpy as np
from tqdm import tqdm

from scripts.utils import calculate_correlation, split_into_tiles


def rebuild_video(gop, num_tiles, max_displacement, quality, frames_info):
    processed_video = []
    reference_frame = None

    for frame_info in tqdm(frames_info, desc="Rebuilding video frames", unit="frame"):
        frame_index = frame_info["frame_index"]
        frame_data = np.array(frame_info["frame_data"], dtype=np.uint8)

        if frame_index % gop == 0:
            processed_video.append(frame_data)
            reference_frame = frame_data
            continue

        if reference_frame is None:
            reference_frame = frame_data

        current_tiles = split_into_tiles(frame_data, num_tiles)
        reference_tiles = split_into_tiles(reference_frame, num_tiles)

        new_frame = frame_data.copy()
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

            if max_corr > quality:
                new_frame[i * tile_height:(i + 1) * tile_height, j * tile_width:(j + 1) * tile_width] = np.mean(
                    frame_data)

        processed_video.append(new_frame)

    return processed_video