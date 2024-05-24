import numpy as np


def encode1(images, gop, n_tiles, quality):
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

# def mse(imageA, imageB):
#     # Calcula el error cuadrático medio entre dos imágenes
#     err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
#     err /= float(imageA.shape[0] * imageA.shape[1])
#     return err
#
#
# def process_images(images, gop_size, tessellation_size, max_displacement):
#     reference_frame = images[0]
#     processed_images = [reference_frame]
#     h, w = tessellation_size
#
#     for i in range(1, len(images)):
#         current_frame = images[i]
#         processed_frame = current_frame.copy()
#         for y in range(0, current_frame.shape[0], h):
#             for x in range(0, current_frame.shape[1], w):
#                 # Tesela actual
#                 current_tess = current_frame[y:y + h, x:x + w]
#                 min_mse = float('inf')
#                 best_match = None
#
#                 # Buscar la mejor coincidencia en el marco anterior dentro del desplazamiento permitido
#                 for dy in range(-max_displacement, max_displacement + 1):
#                     for dx in range(-max_displacement, max_displacement + 1):
#                         yy = y + dy
#                         xx = x + dx
#                         if yy < 0 or yy + h > current_frame.shape[0] or xx < 0 or xx + w > current_frame.shape[1]:
#                             continue
#                         ref_tess = reference_frame[yy:yy + h, xx:xx + w]
#                         error = mse(current_tess, ref_tess)
#                         if error < min_mse:
#                             min_mse = error
#                             best_match = (dy, dx)
#
#                 # Si la mejor coincidencia tiene un error bajo, reemplazar la tesela con el valor medio de la imagen
#                 if min_mse < 1000:  # Umbral de error ajustable
#                     processed_frame[y:y + h, x:x + w] = np.mean(current_frame)
#
#         processed_images.append(processed_frame)
#
#     return processed_images