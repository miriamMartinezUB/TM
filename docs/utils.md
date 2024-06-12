# **Utils**

## compression_ratio_info
FUNCTIONS

    get_compression_ratio(input_zip_folder, output_zip_folder)
        Calcula el ratio de compresión entre dos carpetas ZIP.
        
        Args:
            input_zip_folder (str): Ruta de la carpeta ZIP original.
            output_zip_folder (str): Ruta de la carpeta ZIP comprimida.
        
        Returns:
            float: Ratio de compresión (0-1).


## create_video_from_images

FUNCTIONS

    video_from_images(images, fps, file_name)
        Crea un vídeo a partir d'una llista d'imatges.
        
        Args:
            images (list): Llista d'imatges (cada imatge és un array de numpy).
            fps (int): Fotogrames per segon per al vídeo.
        
        Returns:
            No retorna res, però genera un file de sortida que es diu video_salida.avi on es pot veure el vídeo amb els filtres que hàgim aplicat si és que ho hem fet.


## decode 

FUNCTIONS

    rebuild_video(gop, num_tiles, frames_info, processed_video)
        Reconstrueix el vídeo original a partir de la informació dels fotogrames processats.
        
        :param gop: Mida del grup d'imatges (GOP).
        :type gop: int
        :param num_tiles: Nombre de tessel·les en cada dimensió.
        :type num_tiles: int
        :param frames_info: Informació dels fotogrames processats. Cada element és un diccionari que conté l'índex del fotograma i les tessel·les eliminades, incloent-hi els índexs de la tessel·la actual i la millor tessel·la de referència.
        :type frames_info: list[dict]
        :param processed_video: Vídeo processat com una llista de fotogrames.
        :type processed_video: list[numpy.ndarray]
        :return: Vídeo original reconstruït.
        :rtype: list[numpy.ndarray]


## json_utils

FUNCTIONS

    check_video_info_json(folder_path)
    
    get_path(input_path)
    
    save_info_encode(frames_info, gop, num_tiles, max_displacement, quality, fps, filters, filter_conv, input_path)

DATA

    name_json = 'video_info.json'


## open_zip

FUNCTIONS

    open_zip(input_path)
        Obre un arxiu ZIP que conté imatges o fitxers de text.
        
        Args:
            input_path (str): Ruta de l'arxiu ZIP.
        
        Returns:
            list: Una llista d'arrays numpy que contenen les imatges per ordre alfabètic contingudes dins del ZIP.
            list: Una llista de diccionarios que contienen los datos JSON extraídos del ZIP.

## own_codec

FUNCTIONS

    process_video(video, gop, num_tiles, max_displacement, quality)
        Processa un vídeo amb els paràmetres donats.
        
        :param video: Vídeo d'entrada com una llista de fotogrames.
        :type video: list[numpy.ndarray]
        :param gop: Mida del grup d'imatges (GOP).
        :type gop: int
        :param num_tiles: Nombre de tessel·les en cada dimensió.
        :type num_tiles: int
        :param max_displacement: Desplaçament màxim per cercar correlacions.
        :type max_displacement: int
        :param quality: Qualitat mínima de la correlació per considerar una tessel·la.
        :type quality: float
        :return: Una tupla amb el vídeo processat i la informació dels fotogrames.
        :rtype: tuple(list[numpy.ndarray], list[dict])


## parse_filter


FUNCTIONS

    parse_filter(filter_string)
        Analitza una cadena que representa un filtre.
        
        Args:
            filter_string (str): Cadena que representa un filtre. El format esperat és "nom_del_filtre[argument]".
        
        Returns:
            tuple: Una tupla amb el nom del filtre i l'argument opcional. Si no hi ha argument, l'element dret de la tupla serà None.

## parse_images_to_jpeg

FUNCTIONS

    parse_images_to_jpeg(input_files, new_directory_name)
        Converteix les imatges d'entrada a format JPEG i les guarda en un directori nou.
        
        Args:
            input_files (list): Llista de rutes dels arxius d'imatge d'entrada.
            new_directory_name (str): Nom del directori on guardar les imatges convertides.
        
        Returns:
            None

## play_images

FUNCTIONS

    show_images_as_video(image_path, fps, cmap)
        Reprodueix un vídeo a partir d'una seqüència d'imatges amb el nombre de quadres especificat.
        
        Args:
            image_path (list): Ruta on es troben els fotogrames.
            fps (int): Nombre de fotogrames per segon per mostrar el vídeo.
            cmap (str): Mapa de colors utilitzat per mostrar les imatges. Estableix 'gray' per a imatges en escala de grisos.
        
        Returns:
            None




## read_gif

FUNCTIONS

    extract_frames_from_gif(gif_path)
        Extreu els fotogrames d'un fitxer GIF.
        
        :param gif_path: Ruta on es troba el fitxer GIF.
        :type gif_path: str
        :return: Fotogrames del fitxer GIF, com una llista d'imatges.
        :rtype: list



## read_video

FUNCTIONS

    extract_frames_from_video(video_path)
        Extreu els fotogrames d'un vídeo.
        
        :param video_path: Ruta al vídeo.
        :type video_path: str
        :return: Una llista de fotogrames.
        :rtype: list



## utils

FUNCTIONS

    calculate_correlation(tile1, tile2)
        Calcula la correlació entre dues tessel·les utilitzant les seves DCT.
        
        :param tile1: Primera tessel·la.
        :type tile1: numpy.ndarray
        :param tile2: Segona tessel·la.
        :type tile2: numpy.ndarray
        :return: Correlació entre les dues tessel·les.
        :rtype: float
    
    split_into_tiles(image, num_tiles)
        Divideix una imatge en un nombre determinat de tessel·les.
        
        :param image: Imatge d'entrada.
        :type image: numpy.ndarray
        :param num_tiles: Nombre de tessel·les en cada dimensió.
        :type num_tiles: int
        :return: Llista de tessel·les.
        :rtype: list[numpy.ndarray]

## zip_images

FUNCTIONS

    zip_images(directory_name, images, json_file_path=None)
        Comprimeix totes les imatges dins del directori donat, i opcionalment afegeix un arxiu JSON.
        
        :param directory_name: Nom del directori.
        :type directory_name: str
        :param images: Llista d'imatges a comprimir.
        :type images: list
        :param json_file_path: nom del arxiu JSON
        :type json_file_path: str
        :return: None


## zip_images_gif

FUNCTIONS

    zip_images_gif(directory_name, images)
        Comprimeix les imatges en un fitxer ZIP.
        
        :param directory_name: Directori de destinació.
        :type directory_name: str
        :param images: Imatges d'entrada.
        :type images: list
        :return: No hi ha cap retorn, només imprimeix informació.
