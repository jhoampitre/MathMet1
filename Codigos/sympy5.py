import sympy 
from sympy import *
t = symbols("t")
a, b = -1, 1

# Definimos los vectores de la base
base = [Matrix([1]), Matrix([t]), Matrix([t**2]), Matrix([t**3]), Matrix([t**4])]

# Definimos el producto interno del espacio vectorial
def producto(f, g):
    return integrate(f[0]*g[0], (t,a,b))

#Debemos verificar que los vectores son ortogonales
ortogonales = True
for i, vi in enumerate(base):
    for j, vj in enumerate(base):
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

# Procedemos a ortogonalizar el conjunto de vectores
pol = []
for v in base:
    u = v
    for o in pol:
        u-= (producto(v, o) / producto(o, o)) * o
    pol.append(u)
# Mostar el resultado
print("Polinomios ortogonalizados:")
for i, pol in enumerate(pol):
    print(f"P_{i}(t) = {simplify(pol[0])}")

#Repetimos el procedimiento para un producto interno nuevo
def producto_chevy(f, g):
    return integrate(f[0]*g[0]*sqrt(1-t**2), (t,a,b))

ortogonalizados_chevy = []
for k in base:
    q = k
    for o in ortogonalizados_chevy:
        q-= (producto_chevy(k, o) / producto_chevy(o, o)) * o
    ortogonalizados_chevy.append(q)
# Mostar el resultado
print("Polinomios ortogonalizados de Chebyshev:")
for i, pol in enumerate(ortogonalizados_chevy):
    print(f"P_{i}(t) = {simplify(pol[0])}")

import matplotlib.pyplot as plt
import numpy as np 

#Calculamos los coeficientes de la funcion aproximada
h_x = sin(3*t)*(1-t**2)
C_0 = simplify(integrate(1*h_x, (t,a,b)))
C_1 = simplify(integrate(t*h_x, (t,a,b)))
C_2 = simplify(integrate((t**2 - 1/3)*h_x, (t,a,b)))
C_3 = simplify(integrate(t*(t**2 - 3/5)*h_x, (t,a,b)))
C_4 = simplify(integrate((t**4 - 6*t**2/7 + 3/35)*h_x, (t,a,b)))

coeficientes_legendre = [C_0, C_1, C_2, C_3, C_4]
print(coeficientes_legendre)