def rebuild_video(gop, num_tiles, frames_info, processed_video):
    """
    Reconstruye el vídeo original a partir de la información de los frames procesados.

    :param gop: Mida del grupo de imágenes (GOP).
    :type gop: int
    :param num_tiles: Número de tessel·les en cada dimensión.
    :type num_tiles: int
    :param frames_info: Información de los frames procesados.
    :type frames_info: list[dict]
    :param processed_video: Vídeo procesado.
    :type processed_video: list[numpy.ndarray]
    :return: Vídeo original reconstruido.
    :rtype: list[numpy.ndarray]
    """
    rebuilt_video = []
    reference_frame = []

    for frame_idx, frame_info in enumerate(frames_info):
        if frame_idx % gop == 0:
            # Si es una imagen de referencia, añadirla sin modificar
            reference_frame = processed_video[frame_idx].copy()
            rebuilt_video.append(reference_frame)
        else:
            current_frame = processed_video[frame_idx].copy()
            tiles_removed = frame_info["tiles_removed"]

            for tile_removed in tiles_removed:
                # Identificar la celda que se va a rellenar
                i, j = tile_removed["i"], tile_removed["j"]
                tile_height, tile_width = current_frame.shape[0] // num_tiles, current_frame.shape[1] // num_tiles

                # Rellenar la celda con la celda de referencia
                ref_tile = reference_frame[i * tile_height:(i + 1) * tile_height,
                           j * tile_width:(j + 1) * tile_width]

                current_frame[i * tile_height:(i + 1) * tile_height, j * tile_width:(j + 1) * tile_width] = ref_tile

            rebuilt_video.append(current_frame)

    return rebuilt_video