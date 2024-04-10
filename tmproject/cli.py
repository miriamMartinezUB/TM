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

from scripts.open_zip import open_zip


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
@click.option("--fps",
              help='<value> : nombre d’imatges per segon amb les quals és reproduirà el vídeo.')
@click.option("--binarization",
              help='<value> : p.ex. per un filtre puntual de binarització utilitzant el valor llindar indicat.')
@click.option("--negative",
              help='p.ex. per un filtre puntual negatiu sobre la imatge.')
@click.option("--averaging",
              help='<value>: p.ex aplicació d’un filtre convolucional d’averaging en zones de value x value.')
@click.option("--n-tiles",
              help='<value,...> : nombre de tessel·les en la qual dividir la imatge. Es poden indicar diferents '
                   'valors per l’eix vertical i horitzontal, o bé especificar la mida de les tessel·les en píxels.')
@click.option("--seek-range",
              help='<value> : desplaçament màxim en la cerca de tessel·les coincidents.')
@click.option("--gop",
              help='<value> : nombre d’imatges entre dos frames de referència')
@click.option("--quality",
              help='<value> : factor de qualitat que determinarà quan dos tessel·les és consideren coincidents.')
@click.option('-b', "--batch",
              help='en aquest mode no s’obrirà cap finestra del reproductor de vídeo. Ha de permetre executar el '
                   'còdec a través de Shell scripts per avaluar de forma automatitzada el rendiment de l’algorisme '
                   'implementat en funció dels diferents paràmetres de configuració.')
@click.help_option('--help', '-h')
@click.command()
def main(input_path, output_path, encode_arg, decode_arg, fps, binarization, negative, averaging, n_tiles, seek_range,
         gop, quality, batch):
    image_path_files = []
    if input_path:
        # Enter with -i argument
        image_path_files = open_zip(input_path)
    else:
        click.echo("Hello, World!")


if __name__ == "__main__":
    main()