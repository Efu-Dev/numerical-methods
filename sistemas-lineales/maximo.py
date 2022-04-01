# Busqueda de Máximo - Diego Faria
# Se buscará el máximo de cada fila.

import sys

A = [[1, 2, 3], [9, 12, 8], [5, -5, -2]]
maxs = {}

for i in range(len(A)):
    max = sys.float_info.min

    for j in range(len(A[i])):
        current = A[i][j]
        if max < current:
            max = current
            pos = [i+1, j+1]
    
    maxs[i+1] = {"max": max, "index": pos}

print(maxs)