import json
import os
from pathlib import Path
from zipfile import ZipFile

from skimage import io
from tqdm import tqdm


def open_zip(input_path):
    """
    Obre un arxiu ZIP que conté imatges o fitxers de text.

    Args:
        input_path (str): Ruta de l'arxiu ZIP.

    Returns:
        list: Una llista d'arrays numpy que contenen les imatges per ordre alfabètic contingudes dins del ZIP.
        list: Una llista de diccionarios que contienen los datos JSON extraídos del ZIP.
    """
    zip_path = Path(input_path)
    image_path_files = []
    json_data_map = {}

    output_dir = zip_path.parent / zip_path.stem

    with ZipFile(zip_path, 'r') as zip_file:
        zip_file.extractall(output_dir)

    # Obtener la lista de archivos dentro del directorio extraído
    file_paths = list(output_dir.iterdir())

    # Inicializar la barra de progreso
    progress_bar = tqdm(file_paths, desc="Extracting files", unit="file")

    for file_path in progress_bar:
        if file_path.is_file():
            file_ext = file_path.suffix
            if file_ext == '.png':
                image_path_files.append(str(file_path))
            elif file_ext == '.txt':
                with open(file_path, 'r') as file:
                    content = file.read()
                    print(f"Content of '{file_path.name}':")
                    print(content)
            elif file_ext == '.json':
                with open(file_path, 'r') as json_file:
                    json_data = json.load(json_file)
                    json_data_map[str(file_path)] = json_data
            else:
                raise Exception('Unsupported file extension found in the ZIP archive.')

    # Ordenar los archivos de imagen por nombre de archivo
    image_path_files.sort(key=lambda x: os.path.basename(x))

    # Leer las imágenes desde los archivos de imagen
    images = [io.imread(image_path) for image_path in image_path_files]

    return images, json_data_map