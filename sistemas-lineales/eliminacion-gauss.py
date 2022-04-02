# Busqueda de Máximo - Diego Faria
# Se aplicará la eliminación Gaussiana a una matriz m con resultados b.

def getvals(m):
    for i in range(len(m)):
        for j in range(len(m[i]) - 1):
            if m[i][j] != 0:
                x = m[i][j]
        
        m[i] = [y/x for y in m[i]]
    
    return m

def printvals(m):
    l = len(m[0]) - 1
    for i in range(len(m)):
        print(f"x{i+1} = {m[i][l]}")


m = [[-1, 2, -5], 
     [1, -1, 3]]

i = 0
for j in range(len(m[0]) - 1): # For each COLUMN...
    ac = len(m) - 1
    while 0 <= ac: # Starting by the last row...
        pivot = -m[ac][j]/m[i][j]
        current = [pivot*x for x in m[i]]

        if ac != i: # If it's not ane element of the diagonal...
            for k  in range(len(m[i])):
                m[ac][k] = m[ac][k] + current[k]
        
        ac -= 1

    i += 1

m = getvals(m)
printvals(m)