import numpy as np
from scipy.fftpack import dct


def calculate_correlation(tile1, tile2):
    """
    Calcula la correlació entre dues tessel·les utilitzant les seves DCT.

    :param tile1: Primera tessel·la.
    :type tile1: numpy.ndarray
    :param tile2: Segona tessel·la.
    :type tile2: numpy.ndarray
    :return: Correlació entre les dues tessel·les.
    :rtype: float
    """
    dct1 = _calculate_dct(tile1)
    dct2 = _calculate_dct(tile2)
    return np.corrcoef(dct1.flatten(), dct2.flatten())[0, 1]


def split_into_tiles(image, num_tiles):
    """
    Divideix una imatge en un nombre determinat de tessel·les.

    :param image: Imatge d'entrada.
    :type image: numpy.ndarray
    :param num_tiles: Nombre de tessel·les en cada dimensió.
    :type num_tiles: int
    :return: Llista de tessel·les.
    :rtype: list[numpy.ndarray]
    """
    height, width = image.shape[:2]
    tile_height = height // num_tiles
    tile_width = width // num_tiles
    tiles = []

    for i in range(num_tiles):
        for j in range(num_tiles):
            tile = image[i * tile_height:(i + 1) * tile_height, j * tile_width:(j + 1) * tile_width]
            tiles.append(tile)

    return tiles


def _calculate_dct(tile):
    """
    Calcula la DCT (Transformada Discreta del Cosinus) d'una tessel·la.

    :param tile: Tessel·la d'entrada.
    :type tile: numpy.ndarray
    :return: DCT de la tessel·la.
    :rtype: numpy.ndarray
    """
    return dct(dct(tile.T, norm='ortho').T, norm='ortho')