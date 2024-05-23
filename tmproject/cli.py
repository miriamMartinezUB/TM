"""
Your CLI code goes here, here you should copy the first `S1_0_cli_command_example.py` script and paste it here, remove
the `if __name__ == '__main__':` statement and preserve the `main` function, which is a Click command.

Remember to import the main function from the `__main__.py` file, and call it here.

Also, remember you can create a tree of python submodules to organize your code, for example, you can create a
`commands` submodule to store all the commands of your CLI application, and then import them here. Or you can keep them
here and create something like a `utils.py` file to store useful functions and classes that are used repeatedly
by the commands.
"""
import os

import click

from scripts.average_filter import average_filter
from scripts.binarization_filter import binarization_filter
from scripts.contrast_stretching import contrast_stretching
from scripts.gradient_filter import gradient_filter
from scripts.grayscale_filter import grayscale_filter
from scripts.negative_filter import negative_filter
from scripts.open_zip import open_zip
from scripts.parse_filter import parse_filter
from scripts.parse_images_to_jpeg import parse_images_to_jpeg
from scripts.play_images import show_images_as_video
from scripts.sepia_filter import sepia_filter
from scripts.sobel_filter import sobel_filter
from scripts.zip_images import zip_images


@click.option('-i', "--input", 'input_path',
              help='<path to file.zip> : Fitxer d’entrada. Argument obligatori.')
@click.option('-o', "--output", 'output_path',
              help='<path to file> : Nom del fitxer en format propi amb la seqüència d’imatges de sortida i la '
                   'informació necessària per la descodificació.')
@click.option('-e', "--encode", 'encode_arg',
              help='Argument que indica que s’haurà d’aplicar la codificació sobre el conjunt d’imatges d’input i '
                   'guardar el resultat al lloc indicat per output. En acabar, s’ha de procedir a reproduir el '
                   'conjunt d’imatges sense codificar (input). Per una descripció detallada del que ha de realitzar, '
                   'vegi l’apartat --Encode.')
@click.option('-d', "--decode", 'decode_arg',
              help='Argument que indica que s’haurà d’aplicar la descodificació sobre el conjunt d’imatges d’input '
                   'provinents d’un fitxer en format propi i reproduir el conjunt d’imatges descodificat (output). '
                   'Per una descripció detallada del que ha de realitzar, vegi l’apartat --Decode.')
@click.option("--fps", default=30,
              help='<value> : nombre d’imatges per segon amb les quals és reproduirà el vídeo.')
@click.option("--n-tiles",
              help='<value,...> : nombre de tessel·les en la qual dividir la imatge. Es poden indicar diferents '
                   'valors per l’eix vertical i horitzontal, o bé especificar la mida de les tessel·les en píxels.')
@click.option("--seek-range",
              help='<value> : desplaçament màxim en la cerca de tessel·les coincidents.')
@click.option("--gop",
              help='<value> : nombre d’imatges entre dos frames de referència')
@click.option("--quality",
              help='<value> : factor de qualitat que determinarà quan dos tessel·les és consideren coincidents.')
@click.option('-f', "--filter", 'filters', multiple=True,
              help='Especifica els filtres a aplicar a les imatges. El format és "nom_del_filtr[argument]".')
@click.option('--filter-conv', 'filter_conv', multiple=True,
              help='Especifica els filtres de convolució a aplicar a les imatges. El format és "nom_del_filtr[argument]".')
@click.help_option('--help', '-h')
@click.command()
def main(input_path, output_path, encode_arg, decode_arg, fps, n_tiles, seek_range,
         gop, quality, filters, filter_conv):
    images = []
    cmap = None
    if input_path:
        images = open_zip(input_path)
    if fps:
        if not os.path.exists('data/raw/Cubo'):
            raise Exception('You need to run "python -m tmproject.cli -i data/raw/Cubo.zip" first')
    if filters:
        filter_list = filters[0].split(',')
        for f in filter_list:
            filter_name, argument = parse_filter(f)
            filter_name = filter_name.strip()
            if filter_name == 'negative':
                images = negative_filter(images)
            elif filter_name == 'sepia':
                images = sepia_filter(images)
            elif filter_name == 'binarization':
                images = binarization_filter(images, threshold=70 if argument is None else argument)
            elif filter_name == 'grayscale':
                images = grayscale_filter(images)
                cmap = "gray"
            elif filter_name == 'contrast_stretching':
                images = contrast_stretching(images)
            else:
                raise Exception(f"We don't support {filter_name} filter")
    if filter_conv:
        filter_conv_list = filter_conv[0].split(',')
        for f in filter_conv_list:
            filter_name, argument = parse_filter(f)
            if filter_name == 'sobel':
                images = sobel_filter(images)
                cmap = "gray"
            elif filter_name == 'averaging':
                images = average_filter(images, kernel_size=3 if argument is None else int(argument))
            elif filter_name == 'gradient':
                images = gradient_filter(images)
            else:
                raise Exception(f"We don't support {filter_name} filter conv")

    if output_path:
        if len(images) == 0:
            raise Exception("You must indicate an input path before --output")
        parse_images_to_jpeg(images, output_path)
        zip_images(output_path)
    else:
        show_images_as_video(images, fps, cmap)


if __name__ == "__main__":
    main()