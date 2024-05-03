

def negative_filter(images):
    negative_images = []
    for image in images:
        inverted_image_np = 255 - image
        negative_images.append(inverted_image_np)
    return negative_images