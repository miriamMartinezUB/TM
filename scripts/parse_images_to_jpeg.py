import os

from PIL import Image


def parse_images_to_jpeg(input_files, new_directory_name):
    """
    Converteix les imatges d'entrada a format JPEG i les guarda en un directori nou.

    Args:
        input_files (list): Llista de rutes dels arxius d'imatge d'entrada.
        new_directory_name (str): Nom del directori on guardar les imatges convertides.

    Returns:
        None
    """
    directory_name_without_extension = os.path.splitext(new_directory_name)[0]

    os.makedirs(directory_name_without_extension, exist_ok=True)

    for file in input_files:
        if os.path.splitext(file)[1].lower() == '.jpg' or os.path.splitext(file)[1].lower() == '.jpeg':
            # Si ya es una imagen JPEG, simplemente la copiamos al nuevo directorio
            os.system(f'cp {file} {os.path.join(directory_name_without_extension, os.path.basename(file))}')
        else:
            # Si no es JPEG, la abrimos y la guardamos como JPEG en el nuevo directorio
            img = Image.open(file)
            img.save(
                os.path.join(directory_name_without_extension, os.path.splitext(os.path.basename(file))[0] + '.jpg'),
                'JPEG')