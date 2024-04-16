import os

from PIL import Image


def parse_images_to_jpeg(input_files, new_directory_name):
    os.makedirs(new_directory_name, exist_ok=True)

    for file in input_files:
        if os.path.splitext(file)[1].lower() == '.jpg' or os.path.splitext(file)[1].lower() == '.jpeg':
            # Si ya es una imagen JPEG, simplemente la copiamos al nuevo directorio
            os.system(f'cp {file} {os.path.join(new_directory_name, os.path.basename(file))}')
        else:
            # Si no es JPEG, la abrimos y la guardamos como JPEG en el nuevo directorio
            img = Image.open(file)
            img.save(os.path.join(new_directory_name, os.path.splitext(os.path.basename(file))[0] + '.jpg'), 'JPEG')