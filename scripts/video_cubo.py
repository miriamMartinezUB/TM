import os

from PIL import Image
from pathlib import Path
from zipfile import ZipFile
import cv2
import numpy as np

def zip_images(directory_name):
    with zipfile.ZipFile(f"{directory_name}.zip", 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(directory_name):
            for file in files:
                zip_file.write(os.path.join(root, file),
                               arcname=os.path.join(os.path.relpath(root, directory_name), file))

def open_zip(input_path):
    zip_path = Path(input_path)
    image_path_files = []

    output_dir = zip_path.parent / zip_path.stem

    with ZipFile(zip_path, 'r') as zip_file:
        zip_file.extractall(output_dir)

    for file_path in output_dir.iterdir():
        if file_path.is_file():
            file_ext = file_path.suffix
            if file_ext == '.png':
                print(f"Image file path '{file_path}' added")
                image_path_files.append(file_path)
            elif file_ext == '.txt':
                with open(file_path, 'r') as file:
                    content = file.read()
                    print(f"Content of '{file_path.name}':")
                    print(content)
            else:
                raise Exception('We only support txt and png extensions, check the content on your zip')

    return image_path_files


images = open_zip("data/raw/Cubo.zip")

video = cv2.VideoWriter('video_salida.wmv', cv2.VideoWriter_fourcc(*'mp4v'), 2, (width, height))
for i in images:
    video.write(cv2.imread(i))
video.release()