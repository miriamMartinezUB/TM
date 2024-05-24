import os
from pathlib import Path
from zipfile import ZipFile

from skimage import io


def open_zip(input_path):
    """
    Obre un arxiu ZIP que conté imatges o fitxers de text.

    Args:
        input_path (str): Ruta de l'arxiu ZIP.

    Returns:
        list: Una llista d'arrays numpy que contenen les imatges per ordre alfabètic contingudes dins del ZIP.
    """
    zip_path = Path(input_path)
    image_path_files = []

    output_dir = zip_path.parent / zip_path.stem

    with ZipFile(zip_path, 'r') as zip_file:
        zip_file.extractall(output_dir)

    for file_path in output_dir.iterdir():
        if file_path.is_file():
            file_ext = file_path.suffix
            if file_ext == '.png':
                image_path_files.append(str(file_path))
            elif file_ext == '.txt':
                with open(file_path, 'r') as file:
                    content = file.read()
                    print(f"Content of '{file_path.name}':")
                    print(content)
            else:
                raise Exception('We only support txt and png extensions, check the content on your zip')
    image_path_files.sort(key=lambda x: os.path.basename(x))
    images = []
    for image_path in image_path_files:
        images.append(io.imread(image_path))
    return images