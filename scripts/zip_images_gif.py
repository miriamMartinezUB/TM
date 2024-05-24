import os
import zipfile

from tqdm import tqdm


def zip_images_gif(directory_name, images):
    """
    Comprimeix les imatges en un fitxer ZIP.

    :param directory_name: Directori de destinació.
    :type directory_name: str
    :param images: Imatges d'entrada.
    :type images: list
    :return: No hi ha cap retorn, només imprimeix informació.
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