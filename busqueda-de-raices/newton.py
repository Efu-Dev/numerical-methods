# Método de Newton-Raphson - Diego Faria
# Clase #4 Métodos Numéricos

import math
from numpy import double

def funcion(x):
    return x**x - 10 # Definición de la función f(x)

def derivada(x):
    return x**x*(math.log(x)+1) # Definición de la deriviada f'(x)

xi = double(input("Ingrese x0 = "))
iteraciones = int(input("Iteraciones: "))

try:
    for _ in range(iteraciones):
        xi = xi - funcion(xi)/derivada(xi)
except:
    print("El método falló.")
else:    
    print(f"Aproximación al corte en X={xi}\nf({xi})={funcion(xi)}")