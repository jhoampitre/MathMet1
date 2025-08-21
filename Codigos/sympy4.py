import sympy 
from sympy import *
t = symbols("t")
a, b = -1, 1
# Definimos las funciones base como vectores
base = [Matrix([1]), Matrix([t]), Matrix([t**2]), Matrix([t**3]), Matrix([t**4])]

# Definimos el producto interno
def producto(f, g):
    return integrate(f[0]*g[0]*sqrt(1-t**2), (t, a, b))

# Realizamos Gram-Schmidt
ortogonalizados = []
for v in base:
    u = v
    for o in ortogonalizados:
        u = u - (producto(v, o) / producto(o, o)) * o
    ortogonalizados.append(u)

# Mostar el resultado
print("Polinomios ortogonalizados:")
for i, pol in enumerate(ortogonalizados):
    print(f"P_{i}(t) = {simplify(pol[0])}")

#Verificamos que efectivamente la base sea ortogonal
e1=ortogonalizados[0]
e2=ortogonalizados[1]
e3=ortogonalizados[2]
e4=ortogonalizados[3]
e5=ortogonalizados[4]

vectores = [e1, e2, e3, e4, e5]

ortogonales = True
for i, vi in enumerate(vectores):
    for j, vj in enumerate(vectores):
        if j > i: # Comparamos solo una vez para j > i
            resultado = producto(vi, vj)
            print(f"Producto interno de e{i+1} y e{j+1}: {resultado}")
            if resultado != 0:
                ortogonales = False

# Mostrar el resultado
if ortogonales:
    print("El conjunto de vectores es ortogonal.")
else:
    print("El conjunto de vectores NO es ortogonal.")