def parse_filter(filter_string):
    """
    Analitza una cadena que representa un filtre.

    Args:
        filter_string (str): Cadena que representa un filtre. El format esperat és "nom_del_filtre[argument]".

    Returns:
        tuple: Una tupla amb el nom del filtre i l'argument opcional. Si no hi ha argument, l'element dret de la tupla serà None.
    """
    if '[' in filter_string:
        parts = filter_string.split('[')
        filter_name = parts[0]
        argument = parts[1][:-1]
        return filter_name, argument
    return filter_string, None