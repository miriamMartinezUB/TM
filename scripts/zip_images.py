import os
import zipfile


def zip_images(directory_name):
    with zipfile.ZipFile(f"{directory_name}.zip", 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(directory_name):
            for file in files:
                zip_file.write(os.path.join(root, file),
                               arcname=os.path.join(os.path.relpath(root, directory_name), file))