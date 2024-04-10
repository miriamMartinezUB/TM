from pathlib import Path
from zipfile import ZipFile


def open_zip(input_path):
    # Define the path of the zip file:
    zip_path = Path(input_path)
    image_path_files = []

    with ZipFile(zip_path, 'r') as zip_file:
        # Get the list of file names inside the zip:
        file_names = zip_file.namelist()

        # Iterate over each file name:
        for file_name in file_names:
            # Open the file from the zip:
            with zip_file.open(file_name) as file:
                # Get the file path inside the zip
                file_path = zip_path / file_name
                # Get the file extension
                file_ext = file_path.suffix
                # If the file is a txt
                if file_ext == '.txt':
                    # Read and process the content of the file:
                    content = file.read().decode('utf-8')

                    # Print the content or do any other processing:
                    print(f"Content of '{file_name}':")
                    print(content)
                # If the file is a PNG image
                elif file_ext == '.png':
                    # Add the file path to the list of image files
                    print(f"Image file path '{file_path}' added")
                    image_path_files.append(file_path)
                else:
                    raise Exception('We only support txt and png extensions, check the content on your zip')

        return image_path_files