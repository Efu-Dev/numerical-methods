# Método de Newton para Multiplicidad Superior - Diego Faria
# Clase #8 Métodos Numéricos

def f(x):
    return 4*x**3+4*x**2-7*x+2 # Definición de F(x)

def df(x):
    return 12*x**2+8*x-7 # Primer orden de F(x)

def d2f(x):
    return 24*x+8 # Segundo orden de F(x)

x = float(input("Ingrese valor de x cercano a un 0: "))
it = int(input("Ingrese las iteraciones: "))

for _ in range(it):
    try:
        fx = f(x)
        
        if(fx == 0):
            break

        dfx = df(x)
        x = x - (fx*dfx/(dfx**2-fx*d2f(x)))
    except:
        print("No se necesitan más iteraciones.")
        break

    print(f"{_+1}. F({x}) = {f(x)}")