import os
import zipfile

from PIL import Image
from tqdm import tqdm


def zip_images(directory_name, images, json_file_path=None):
    """
    Comprimeix totes les imatges dins del directori donat, i opcionalment afegeix un arxiu JSON.

    :param directory_name: Nom del directori.
    :type directory_name: str
    :param images: Llista d'imatges a comprimir.
    :type images: list
    :param json_file_path: nom del arxiu JSON
    :type json_file_path: str
    :return: None
    """
    # Crear un archivo ZIP
    with zipfile.ZipFile(directory_name, 'w') as zipf:
        # Añadir las imágenes al archivo ZIP
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

        # Añadir el archivo JSON al ZIP si se proporciona
        if json_file_path is not None:
            # Agregar el archivo JSON al archivo ZIP
            zipf.write(json_file_path, os.path.basename(json_file_path))

    print(f"Las imágenes se han guardado correctamente en {directory_name}")