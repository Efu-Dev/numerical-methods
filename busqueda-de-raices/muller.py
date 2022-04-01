# Método de Müller - Diego Faria
# Clase #5 Métodos Numéricos

import math

def f(x):
    return x**3 - 13*x - 12 #Definición de f(x)

x0 = float(input("Ingrese x0: "))
x1 = float(input("Ingrese x1: "))
x2 = float(input("Ingrese x2: "))
it = int(input("Ingrese las iteraciones: "))

[f0, f1, f2] = [f(x0), f(x1), f(x2)]

for _ in range(it):
    try:
        d0 = (f1 - f0)/(x1-x0)
        d1 = (f2-f1)/(x2-x1)

        a = (d1-d0)/((x1-x0)+(x2-x1))
        b = a*(x2-x1)+d1
        disc = math.sqrt(b**2-4*a*f2)

        if(math.fabs(b + disc) > math.fabs(b - disc)):
            x3 = x2 + (-2*f2)/(b + disc)
        else:
            x3 = x2 + (-2*f2)/(b - disc)
    except:
        break
    
    [x0,x1,x2] = [x1, x2, x3]
    [f0,f1,f2] = [f(x0),f(x1),f(x2)]
    print(f"{_+1}. F({x2}) = {f(x2)}")