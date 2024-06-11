# FILTERS

## binarization_filter

FUNCTIONS

    binarization_filter(images, threshold)
        Aplica un filtre de binarització a una llista d'imatges.
        
        Args:
            images (list): Llista d'imatges (cada imatge és un array de numpy).
            threshold (int): Llindar per a la binarització (0-255).
        
        Returns:
            list: Llista d'imatges binaritzades com arrays de numpy.

## contrast_stretching

FUNCTIONS

    contrast_stretching(images)
        Aplica l'estirament de contrast a una llista d'imatges.
        
        Args:
            images (list): Llista d'imatges (cada imatge és un array de numpy).
        
        Returns:
            list: Llista d'imatges amb el contrast estirat com arrays de numpy.



## grayscale_filter

FUNCTIONS

    grayscale_filter(images)
        Aplica un filtre d'escala de grisos a una llista d'imatges.
        
        Args:
            images (list): Llista d'imatges (cada imatge és un array de numpy).
        
        Returns:
            list: Llista d'imatges en escala de grisos com arrays de numpy.

## negative_filter

FUNCTIONS

    negative_filter(images)
        Aplica un filtre negatiu a una llista d'imatges.
        
        Args:
            images (list): Llista d'imatges (cada imatge és un array de numpy).
        
        Returns:
            list: Llista d'imatges negatives com arrays de numpy.

## sepia_filter

FUNCTIONS

    sepia_filter(images)
        Aplica un filtre sépia a una llista d'imatges.
        
        Args:
            images (list): Llista d'imatges (cada imatge és un array de numpy).
        
        Returns:
            list: Llista d'imatges sépia com arrays de numpy.
