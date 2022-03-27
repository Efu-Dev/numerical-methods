# Método de Punto Fijo - Diego Faria
# Clase #3 Métodos Numéricos

from numpy import double
import math

def funcion(x):
    return x**3+4*x**2-10 # Colocar aquí la definición de la función F.

def funcionG(x):
    return math.sqrt(10/(4+x)) # Colocar aquí la definición de la función G.

def derivada(x):
    return -10/(4+x)**2 # Colocar aquí la derivada de la función G.

intervalo = [double(input("Ingrese el menor numero del intervalo: ")),double(input("Ingrese el mayor numero del intervalo: "))]
it = int(input("Iteraciones: "))
x = double(input("Ingrese x0 (en el intervalo): "))
subconjunto = [funcionG(intervalo[0]), funcionG(intervalo[1])]

if(intervalo[0] <= subconjunto[0] and intervalo[1] >= subconjunto[1]):
    for _ in range(it):
        x = funcionG(x)
    
    if(math.fabs(derivada(x)) < 1):
        print(f"Punto de corte en X={x}")
        print(f"F({x}) = {funcion(x)}")
    else:
        print("El método falló.")
else:
    print("Intérvalo inválido")