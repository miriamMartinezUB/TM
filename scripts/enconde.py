import numpy as np


def encode(images, gop, n_tiles, quality):
    def correlate(tile1, tile2):
        # Algorisme de correlació: calcula la suma de les diferències absolutes entre els píxels
        return np.sum(np.abs(tile1 - tile2))

    def eliminate_tiles(img, eliminated_tiles):
        # Elimina les tessel·les marcades i les substitueix pel valor mig de la imatge
        h, w, _ = img.shape
        for j, k in eliminated_tiles:
            tile_h = h // n_tiles
            tile_w = w // n_tiles
            tile = img[j * tile_h:(j + 1) * tile_h, k * tile_w:(k + 1) * tile_w]
            img[j * tile_h:(j + 1) * tile_h, k * tile_w:(k + 1) * tile_w] = np.mean(tile)
        return img

    video = []
    for i in range(len(images)):
        if (i % gop == 0) or (i == 0):
            video.append(images[i])
            continue

        tiles_eliminated = []
        h, w, _ = images[i].shape
        for j in range(n_tiles):
            for k in range(n_tiles):
                tile1 = images[i][j * w // n_tiles:(j + 1) * w // n_tiles, k * h // n_tiles:(k + 1) * h // n_tiles]
                tile2 = images[i - 1][j * w // n_tiles:(j + 1) * w // n_tiles, k * h // n_tiles:(k + 1) * h // n_tiles]
                if correlate(tile1, tile2) > quality:
                    tiles_eliminated.append((j, k))

        img_no_tiles = eliminate_tiles(images[i], tiles_eliminated)
        video.append(img_no_tiles)

    return video