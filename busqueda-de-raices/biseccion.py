# Método de Bisección - Diego Faria
# Clase #2 Métodos Numéricos

import math #En caso de utilizar funciones trigonométricas o logaritmos.
from numpy import double

def funcion(x):
    return x**3+4*x**2-10 # Colocar aquí la definición de la función.

it = int(input("Ingrese las iteraciones: "))
p1 = double(input("Ingrese el primer valor de x (menor): "))
p2 = double(input("Ingrese el segundo valor de x (mayor): "))
v1 = funcion(p1)
v2 = funcion(p2)
r = 0

if p1 < p2 and (v1 > 0 and v2 < 0 or v2 > 0 and v1 < 0): # El algoritmo empieza aquí.
    for _ in range(it):
        m = (p1+p2)/2.0
        mv = funcion(m)

        if mv == 0:
            r = m
            break
        
        if (v1 > 0 and v2 < 0 and mv < 0) or (v2 > 0 and v1 < 0 and mv > 0):
            v2 = mv
            p2 = m
            r = p2
        else:
            v1 = mv
            p1 = m
            r = p1
    
    print(f"Punto de corte en X={r}\nf({r})={funcion(r)}")
else:
    print("No hay raíces en el intervalo dado.")
