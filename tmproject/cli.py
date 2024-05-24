"""
Your CLI code goes here, here you should copy the first `S1_0_cli_command_example.py` script and paste it here, remove
the `if __name__ == '__main__':` statement and preserve the `main` function, which is a Click command.

Remember to import the main function from the `__main__.py` file, and call it here.

Also, remember you can create a tree of python submodules to organize your code, for example, you can create a
`commands` submodule to store all the commands of your CLI application, and then import them here. Or you can keep them
here and create something like a `utils.py` file to store useful functions and classes that are used repeatedly
by the commands.
"""

import click

from scripts.create_video_from_images import video_from_images
from scripts.enconde import encode
from scripts.filters.binarization_filter import binarization_filter
from scripts.filters.contrast_stretching import contrast_stretching
from scripts.filters.grayscale_filter import grayscale_filter
from scripts.filters.negative_filter import negative_filter
from scripts.filters.sepia_filter import sepia_filter
from scripts.filters_conv.average_filter import average_filter
from scripts.filters_conv.blur_filter import blur_filter
from scripts.filters_conv.emboss_filter import emboss_filter
from scripts.filters_conv.gradient_filter import gradient_filter
from scripts.filters_conv.sharpen_filter import sharpen_filter
from scripts.filters_conv.sobel_filter import sobel_filter
from scripts.open_zip import open_zip
from scripts.parse_filter import parse_filter
from scripts.play_images import show_images_as_video
from scripts.zip_images import zip_images
from scripts.read_gif import extract_frames_from_gif
from scripts.read_video import extract_frames_from_video
from scripts.zip_images_gif import zip_images_gif
from scripts.compression import compression
from scripts.own_codec import process_video

@click.option('-i', "--input", 'input_path',
              help='<path to file.zip> : Fitxer d’entrada. Argument obligatori.')
@click.option('-o', "--output", 'output_path',
              help='<path to file> : Nom del fitxer en format propi amb la seqüència d’imatges de sortida i la '
                   'informació necessària per la descodificació.')
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
def main(input_path, output_path, fps, n_tiles, seek_range, gop, quality, filters, filter_conv):
    _images = []
    _cmap = None
    _fps = 30 if fps is None else fps
    _gop = 10 if gop is None else gop
    _n_tiles = 4 if n_tiles is None else n_tiles
    _quality = 1e5 if quality is None else quality

    if input_path:
        if input_path.endswith('.gif'):
            _images = extract_frames_from_gif(input_path)
        elif input_path.endswith('.avi') or input_path.endswith('.mp4') or input_path.endswith('.mpeg'):
            _images = extract_frames_from_video(input_path)
        else:
            _images = open_zip(input_path)

    if len(_images) == 0:
        raise Exception('You must import something not empty')

    if filters:
        filter_list = filters[0].split(',')
        for f in filter_list:
            filter_name, argument = parse_filter(f)
            filter_name = filter_name.strip()
            if filter_name == 'negative':
                _images = negative_filter(_images)
            elif filter_name == 'sepia':
                _images = sepia_filter(_images)
            elif filter_name == 'binarization':
                _images = binarization_filter(_images, threshold=70 if argument is None else argument)
            elif filter_name == 'grayscale':
                _images = grayscale_filter(_images)
                _cmap = "gray"
            elif filter_name == 'contrast_stretching':
                _images = contrast_stretching(_images)
            else:
                raise Exception(f"We don't support {filter_name} filter")

    if filter_conv:
        filter_conv_list = filter_conv[0].split(',')
        for f in filter_conv_list:
            filter_name, argument = parse_filter(f)
            if filter_name == 'sobel':
                _images = sobel_filter(_images)
                _cmap = "gray"
            elif filter_name == 'averaging':
                _images = average_filter(_images)
            elif filter_name == 'gradient':
                _images = gradient_filter(_images)
            elif filter_name == 'emboss':
                _images = emboss_filter(_images)
            elif filter_name == 'sharpen':
                _images = sharpen_filter(_images)
            elif filter_name == 'blur':
                _images = blur_filter(_images)
            else:
                raise Exception(f"We don't support {filter_name} filter conv")

    if gop:
        _images = process_video(_images, int(gop), 12, 1)
    if output_path:
        if input_path.endswith('.gif'):
            zip_images_gif(output_path, _images)
        else:
            zip_images(output_path, _images)
    else:
        show_images_as_video(_images, _fps, _cmap)


if __name__ == "__main__":
    main()