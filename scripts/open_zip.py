from pathlib import Path
from zipfile import ZipFile


def open_zip(input_path):
    # Define the path of the zip file:
    zip_path = Path(input_path)

    with ZipFile(zip_path, 'r') as zip_file:
        # Get the list of file names inside the zip:
        file_names = zip_file.namelist()

        # Iterate over each file name:
        for file_name in file_names:
            # Open the file from the zip:
            with zip_file.open(file_name) as file:
                # Read and process the content of the file:
                content = file.read().decode('utf-8')

                # Print the content or do any other processing:
                print(f"Content of '{file_name}':")
                print(content)


if __name__ == '__main__':
    open_zip('data/raw/Cubo.zip')