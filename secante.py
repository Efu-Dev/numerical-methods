# Método de la Secante - Diego Faria
# Clase #4 Métodos Numéricos

def f(x):
    return x**3+4*x**2-10

x0 = float(input("Ingrese x0: "))
x1 = float(input("Ingrese x1: "))
it = int(input("Ingrese las iteraciones: "))

if(x0 < x1 and (f(x0) > 0 and f(x1) < 0 or f(x0) < 0 and f(x1) > 0)):
    try:
        for _ in range(it):
            [x0,x1] = [x1, x1 - (f(x1)*(x0-x1))/(f(x0)-(f(x1)))]
    except:
        pass
    
    print(f"F({x1}) = {f(x1)}")
else:
    print("Puntos inválidos.")