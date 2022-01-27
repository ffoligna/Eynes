# Crear una matriz de 5x5 randomizada con números enteros,
# encontrar secuencia de 4 números consecutivos horizontal o vertical
# y si se encuentra mostrar la posición inicial y final.

from random import randint


def generador_matriz(fila, columna):
    return [[randint(0, 5) for c in range(columna)] for r in range(fila)]


def consecutivos_en_fila(matriz, cantidad):

    for indice_fila in range(len(matriz)):

        numeros_consecutivos = 1
        numero_anterior = None

        for indice_columna in range(len(matriz[indice_fila])):

            if (matriz[indice_fila][indice_columna] - 1) == numero_anterior:
                numeros_consecutivos += 1
                if numeros_consecutivos == cantidad:
                    print(f"""
Fila con {cantidad} números consecutivos encontrada!!!
Inicio = (fila = {indice_fila}, columna = {indice_columna - cantidad + 1})
Fin = (fila = {indice_fila}, columna = {indice_columna})""")

                    return [(indice_fila, indice_columna - cantidad + 1),
                    (indice_fila, indice_columna)]
            else:
                numeros_consecutivos = 1
            
            numero_anterior = matriz[indice_fila][indice_columna]
    else:
        print("""
# No se encontraron números consecutivos en las filas esta matriz.""")

        return (-1, -1)


def consecutivos_en_columna(matriz, cantidad):

    for indice_columna in range(len(matriz[0])):

        numeros_consecutivos = 1
        numero_anterior = None

        for indice_fila in range(len(matriz)):

            if (matriz[indice_fila][indice_columna] - 1) == numero_anterior:
                numeros_consecutivos += 1
                if numeros_consecutivos == cantidad:
                    print(f"""
Columna con {cantidad} números consecutivos encontrada!!!
Inicio = (fila = {indice_fila - cantidad + 1}, columna = {indice_columna})
Fin = (fila = {indice_fila}, columna = {indice_columna})""")

                    return [(indice_fila - cantidad + 1, indice_columna),
                    (indice_fila, indice_columna)]
            else:
                numeros_consecutivos = 1
            
            numero_anterior = matriz[indice_fila][indice_columna]
    else:
        print("""
# No se encontraron números consecutivos en las columnas de esta matriz.""")

        return (-1, -1)


mi_matriz = generador_matriz(5, 5)

print(mi_matriz)

ubicacion_fila = consecutivos_en_fila(mi_matriz, 4)
ubicacion_columna = consecutivos_en_columna(mi_matriz, 4)
