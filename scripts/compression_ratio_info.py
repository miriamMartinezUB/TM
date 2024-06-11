import os


def get_compression_ratio(input_zip_folder, output_zip_folder):
    """
    Calcula el ratio de compresión entre dos carpetas ZIP.

    Args:
        input_zip_folder (str): Ruta de la carpeta ZIP original.
        output_zip_folder (str): Ruta de la carpeta ZIP comprimida.

    Returns:
        float: Ratio de compresión (0-1).
    """
    # Obtener el tamaño original de la carpeta sin comprimir
    input_size = os.path.getsize(input_zip_folder)

    # Obtener el tamaño del archivo comprimido
    output_size = os.path.getsize(output_zip_folder)

    # Calcular el ratio de compresión
    ratio_compresion = (input_size - output_size) / input_size

    return ratio_compresion