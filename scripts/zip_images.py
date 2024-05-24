import os
import zipfile

from PIL import Image
from tqdm import tqdm  # Importing the tqdm library


def zip_images(directory_name, images):
    """
    Comprimeix totes les imatges dins del directori donat.

    :param directory_name: Nom del directori.
    :type directory_name: str
    :param images: Llista d'imatges a comprimir.
    :type images: list
    :return: None
    """
    # Crear un archivo ZIP
    with zipfile.ZipFile(directory_name, 'w') as zipf:
        # Initialize the progress bar
        for i, image in enumerate(tqdm(images, desc="Zipping images", unit="image")):
            # Convertir la imagen a formato PIL para guardarla
            pil_image = Image.fromarray(image)

            # Crear un nombre temporal para la imagen
            temp_image_path = f"image_{i}.png"

            # Guardar la imagen temporalmente
            pil_image.save(temp_image_path)

            # Agregar la imagen al archivo ZIP
            zipf.write(temp_image_path, os.path.basename(temp_image_path))

            # Eliminar la imagen temporal
            os.remove(temp_image_path)

    print(f"Las imágenes se han guardado correctamente en {directory_name}")