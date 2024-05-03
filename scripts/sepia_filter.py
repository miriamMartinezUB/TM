import numpy as np


def sepia_filter(images):
    sepia_images = []
    sepia_matrix = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131],
                             ])

    for image in images:
        im_sepia = image @ sepia_matrix.T
        sepia_images.append(im_sepia/255)
    return sepia_images