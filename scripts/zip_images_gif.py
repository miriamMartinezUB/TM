import os
import zipfile
from tqdm import tqdm

def zip_images_gif(directory_name, images):
    """
    :param directory_name: destination directory
    :param images: input images
    :return: no return, only prints info
    """
    # Crear un archivo ZIP
    with zipfile.ZipFile(directory_name, 'w') as zipf:
        # Initialize the progress bar
        for i, image in enumerate(tqdm(images, desc="Zipping images", unit="image")):
            # Crear un nombre temporal para la imagen
            temp_image_path = f"image_{i}.png"

            # Guardar la imagen temporalmente
            image.save(temp_image_path)

            # Agregar la imagen al archivo ZIP
            zipf.write(temp_image_path, os.path.basename(temp_image_path))

            # Eliminar la imagen temporal
            os.remove(temp_image_path)

    print(f"Las imágenes se han guardado correctamente en {directory_name}")