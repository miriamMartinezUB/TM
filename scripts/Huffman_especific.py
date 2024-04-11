import heapq
from collections import defaultdict

class NodoHuffman:
    def __init__(self, simbolo, probabilidad):
        self.simbolo = simbolo
        self.probabilidad = probabilidad
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.probabilidad < otro.probabilidad

def construir_arbol_huffman(tabla_simbolos):
    heap = [NodoHuffman(simbolo, probabilidad) for simbolo, probabilidad in tabla_simbolos]
    heapq.heapify(heap)

    while len(heap) > 1:
        nodo_izquierda = heapq.heappop(heap)
        nodo_derecha = heapq.heappop(heap)

        nodo_intermedio = NodoHuffman(None, nodo_izquierda.probabilidad + nodo_derecha.probabilidad)
        nodo_intermedio.izquierda = nodo_izquierda
        nodo_intermedio.derecha = nodo_derecha

        heapq.heappush(heap, nodo_intermedio)

    return heap[0]

def generar_codigos_huffman(arbol_huffman, prefijo="", codigos=None):
    if codigos is None:
        codigos = {}
    if arbol_huffman.simbolo is not None:
        codigos[arbol_huffman.simbolo] = prefijo
    if arbol_huffman.izquierda is not None:
        generar_codigos_huffman(arbol_huffman.izquierda, prefijo + "0", codigos)
    if arbol_huffman.derecha is not None:
        generar_codigos_huffman(arbol_huffman.derecha, prefijo + "1", codigos)
    return codigos

def leer_tabla_desde_archivo(archivo):
    tabla_simbolos = []
    with open(archivo, 'r') as f:
        for linea in f:
            simbolo, probabilidad = linea.split()
            tabla_simbolos.append((simbolo, float(probabilidad)))
    return tabla_simbolos

def escribir_tabla_en_archivo(codigos_huffman, archivo):
    with open(archivo, 'w') as f:
        for simbolo, codigo in codigos_huffman.items():
            f.write(f"Símbolo: {simbolo}, Código Huffman: {codigo}\n")

def main():
    archivo_entrada = "input.txt"
    tabla_simbolos = leer_tabla_desde_archivo(archivo_entrada)

    arbol_huffman = construir_arbol_huffman(tabla_simbolos)
    codigos_huffman = generar_codigos_huffman(arbol_huffman)

    print("Tabla de traducción Huffman:")
    for simbolo, codigo in codigos_huffman.items():
        print(f"Símbolo: {simbolo}, Código Huffman: {codigo}")

    archivo_salida = "output.txt"
    escribir_tabla_en_archivo(codigos_huffman, archivo_salida)
    print(f"Tabla de traducción Huffman escrita en el archivo: {archivo_salida}")

if __name__ == "__main__":
    main()