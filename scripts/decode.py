
def rebuild_video(gop, num_tiles, frames_info, processed_video):
    """
    Reconstrueix el vídeo original a partir de la informació dels fotogrames processats.

    :param gop: Mida del grup d'imatges (GOP).
    :type gop: int
    :param num_tiles: Nombre de tessel·les en cada dimensió.
    :type num_tiles: int
    :param frames_info: Informació dels fotogrames processats. Cada element és un diccionari que conté l'índex del fotograma i les tessel·les eliminades, incloent-hi els índexs de la tessel·la actual i la millor tessel·la de referència.
    :type frames_info: list[dict]
    :param processed_video: Vídeo processat com una llista de fotogrames.
    :type processed_video: list[numpy.ndarray]
    :return: Vídeo original reconstruït.
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
                current_i, current_j = tile_removed["current_tile_indices"]
                best_i, best_j = tile_removed["best_tile_indices"]
                tile_height, tile_width = current_frame.shape[0] // num_tiles, current_frame.shape[1] // num_tiles

                # Rellenar la celda con la mejor celda de referencia
                best_tile = reference_frame[best_i * tile_height:(best_i + 1) * tile_height,
                                            best_j * tile_width:(best_j + 1) * tile_width]

                current_frame[current_i * tile_height:(current_i + 1) * tile_height,
                              current_j * tile_width:(current_j + 1) * tile_width] = best_tile

            rebuilt_video.append(current_frame)

    return rebuilt_video
