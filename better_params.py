import itertools
import os
import shutil
import time

# Parámetros a probar
gop_values = [3, 4, 5]
n_tiles_values = [8, 16, 32]
seek_range_values = [1, 2]
quality_values = [0.99, 0.995]

# Combinaciones de parámetros
combinations = list(itertools.product(gop_values, n_tiles_values, seek_range_values, quality_values))

# Archivo de entrada y salida
input_file = "data/raw/Cubo.zip"

# Script a ejecutar
script = "python -m tmproject.cli"

# Resultados
results = []

for combination in combinations:
    folder_path = "data/raw/Cubo"

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        try:
            shutil.rmtree(folder_path)
        except OSError as e:
            print(f"Error al eliminar carpeta: {e}")

    gop, n_tiles, seek_range, quality = combination
    file_name = f"video_g{gop}_nt{n_tiles}_sr{seek_range}_q{quality}"
    command = f"{script} -i {input_file} -e --gop {gop} --n-tiles {n_tiles} --seek-range {seek_range} --quality {quality} -d -g {file_name}"
    print(f"Ejecutando: {command}")

    start_time = time.time()
    os.system(command)
    end_time = time.time()

    processing_time = (end_time - start_time)
    results.append((combination, processing_time))

# Escribir resultados en un archivo de texto
with open("results.txt", "w") as f:
    f.write("Resultados:\n")
    for combination, processing_time in results:
        f.write(
            f"Combination: gop={combination[0]}, n-tiles={combination[1]}, seek-range={combination[2]}, quality={combination[3]}\n")
        f.write(f"Tiempo de procesamiento: {processing_time:.2f} s")
        f.write("\n_______________________________________________________\n\n")

print("Resultados guardados en results.txt")