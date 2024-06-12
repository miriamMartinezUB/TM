# tm-0-blank-project

Això és un repositori base per crear repositoris per l'assignatura de Tecnologies Multimèdia de la Universitat de
Barcelona.

La plantilla bàsica conté els següents fitxers:

```plaintext
tm-project-base/
├── .gitignore
├── README.md
├── tmproject/
│   ├── __init__.py
│   ├── __main__.py
│   └── cli.py
├── scripts/
│   ├── script1.py
│   ├── ...
│   └── scriptN.py
├── requirements.txt
└── setup.py
```

## Creació d'un entorn de Python amb `pyenv`:

Per tal de treballar adecuadament amb aquest repositori, es recomana la creació d'un entorn de Python amb `pyenv`.
Aquesta eina permet tenir diferents versions de Python instal·lades al sistema i crear entorns virtuals:

```bash
# Crear un entorn de Python 3.8.5
pyenv install 3.9.14
pyenv virtualenv 3.9.14 tm
pyenv local tm
```

Comprobar que `pip` i `wheel` estan actualitzats, i instal·lem `ipython`:

```bash
pip install --upgrade pip wheel
pip install ipython
```

## Instal·lació del paquet local com editable:

Per tal de poder importar el paquet `tmcode0` com un mòdul de Python, es pot instal·lar com a paquet editable:

```bash
pip install -e .
```

## Comandes

- S2: Implementació del parser d’arguments en línia de comandes.
    ```bash
    python -m tmproject.cli -h
    ```

- S1: Implementació d’un lector/escriptor de fitxers ZIP i JPEG.
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip
  ```
- Show Video
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip --fps 50
  ```
- Zip images
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip -o data/raw/Cubo_jpeg.zip
  ```
  ```bash
  python -m tmproject.cli --input data/raw/Cubo.zip --output data/raw/Cubo_jpeg.zip
  ```
- Llegir imatges d'un gif
  ```bash
  python -m tmproject.cli -i data/raw/samplegif.gif 
  ```
- Filtre negatiu
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip --filter "negative"
  ```
- Filtre sepia
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip --filter "sepia"
  ```
- Filtre grayscale
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip --filter "grayscale"
  ```
- Filtre contrast_stretching
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip --filter "contrast_stretching"
  ```
- Filtre binarization
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip --filter "binarization"
  ```
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip --filter "binarization[40]"
  ```
- Multiples filters
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip --filter "negative, binarization[150]"
  ```
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip --filter "binarization" --filter-conv "sobel"
  ```
- Filtre sobel
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip --filter-conv "sobel"
  ```
- Encode i decode
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip -e -o data/raw/output.zip
  python -m tmproject.cli -i data/raw/output.zip -d 
  ```

## Demo

## Intro

 ```bash
       python -m tmproject.cli -h
       
      python -m tmproject.cli -i data/raw/Cubo.zip
      
      python -m tmproject.cli -i data/raw/samplegif.gif
  
      python -m tmproject.cli -i data/raw/Cubo.zip --fps 50
 ```

## Filtros

  ```bash
  python -m tmproject.cli -i data/raw/sample.mp4 --filter "negative"
  
  python -m tmproject.cli -i data/raw/sample.avi --filter "sepia"

  python -m tmproject.cli -i data/raw/Cubo.zip --filter "negative, binarization[150]"
  
  python -m tmproject.cli -i data/raw/Cubo.zip --filter "negative" --filter-conv "blur"

  ```

## Encode

  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip -e -o data/raw/output.zip
  
  python -m tmproject.cli -i data/raw/Cubo.zip -e --n-tiles 6 -o data/raw/output.zip
  
  python -m tmproject.cli -i data/raw/Cubo.zip -e --filter "negative"  -o data/raw/output_filter.zip
  
  python -m tmproject.cli -i data/raw/Cubo.zip -e --filter "negative" --filter-conv "blur" -o data/raw/output_filter_and_conv.zip
  ```

## Decode

  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip -e -o data/raw/output.zip -d
  
  python -m tmproject.cli -i data/raw/output.zip -d
  
  python -m tmproject.cli -i data/raw/output_filter.zip -d
  
  python -m tmproject.cli -i data/raw/output_filter_and_conv.zip -d
  ```

## BetterParams

  ```bash
  python better_params.py

  ```