import os
import zipfile


def zip_images(directory_name):
    directory_name_without_extension = os.path.splitext(directory_name)[0]
    with zipfile.ZipFile(f"{directory_name}", 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(directory_name_without_extension):
            for file in files:
                zip_file.write(os.path.join(root, file),
                               arcname=os.path.join(os.path.relpath(root, directory_name_without_extension), file))