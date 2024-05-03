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
    python -m tmproject.cli -i data/raw/hola.zip
    ```    
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
- Filtre negatiu
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip --filter "negative"
  ```
- Filtre binarization
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip --filter "binarization"
  ```
- Filtre sobel
  ```bash
  python -m tmproject.cli -i data/raw/Cubo.zip --filter-conv "sobel"
  ```
- Filtre mitjana
  ```bash
  python -m tmproject.cli --averaging data/tmp/Cubo05.png
  ```
- Video amb fps
  ```bash
  python -m tmproject.cli --fps 50
  ```