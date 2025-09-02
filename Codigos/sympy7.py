import sympy as sp
from sympy import Matrix, symbols, legendre, integrate
A, B, x, y = symbols("A B x y")
#Definimos las bases cómo matrices
A = Matrix([1, x, x**2]) # Para la matriz A le corresponde una matriz fila
B = Matrix([[1], [y], [y**2]]) # Para la matriz le corresponde una matriz columna
coeficientes = A*B.T # Definimos los coeficientes de la matriz x^i y y^j
print("a) ",coeficientes)

pol_p = 3 + x + x**2
pol_g = 1 + y 
producto = sp.expand(pol_p*pol_g)
print("b) ",producto)

# Usamos la libreria predefinida con los polinomios de Legendre
legendre_polys = [legendre(0, x), legendre(1, x), legendre(2, x)]
#for i, P in enumerate(legendre_polys):
    #print(f"P_{i}(x) = {P}")

polinomio = x**2 + x + 3
P0 = legendre_polys[0]
P1 = legendre_polys[1]
P2 = legendre_polys[2]

#Calculamos los coeficientes C_n
c_0 = sp.Rational(1, 2) * sp.integrate(polinomio*P0, (x,-1,1))
c_1 = sp.Rational(3,2) * sp.integrate(polinomio*P1, (x,-1,1))
c_2 = sp.Rational(5,2) * sp.integrate(polinomio*P2, (x,-1,1))

#Hallamos la expresión para el polinomio expandido
expresion = c_0*P0 + c_1*P1 + c_2*P2
print("c) ", expresion.simplify())

#Calculamos las bases de los espacios como una expansión en los polinomios de legendre
legendre_polys_y = [legendre(0, y), legendre(1, y), legendre(2, y)]
P0_y = legendre_polys_y[0]
P1_y = legendre_polys_y[1]
P2_y = legendre_polys_y[2]

polinomio_x = 1 + x + x**2
polinomio_y = 1 + y + y**2

cx_0 = sp.Rational(1, 2) * sp.integrate(polinomio_x*P0, (x,-1,1))
cx_1 = sp.Rational(3,2) * sp.integrate(polinomio_x*P1, (x,-1,1))
cx_2 = sp.Rational(5,2) * sp.integrate(polinomio_x*P2, (x,-1,1))

cy_0 = sp.Rational(1, 2) * sp.integrate(polinomio_y*P0_y, (y,-1,1))
cy_1 = sp.Rational(3,2) * sp.integrate(polinomio_y*P1_y, (y,-1,1))
cy_2 = sp.Rational(5,2) * sp.integrate(polinomio_y*P2_y, (y,-1,1))

expansion_x = cx_0*P0 + cx_1*P1 + cx_2*P2
expansion_y = cy_0*P0_y + cy_1*P1_y + cy_2*P2_y

#Representamos los polinomios respectivos como matrices
coeficientes_x = sp.Poly(expansion_x, x).all_coeffs()
coeficientes_y = sp.Poly(expansion_y, y).all_coeffs()
matriz_x = sp.Matrix(coeficientes_x)
matriz_y = sp.Matrix(coeficientes_y)
matriz_de_coeficientes = matriz_x*matriz_y.T
#print("d) ", matriz_de_coeficientes) #NO LO ENTENDÍ COMPLETAMENTE

#Ejercicio 4 con ayuda

def componentes_tensor_legendre():

    # Creamos una matriz 3x3 para las componentes
    matriz_componentes = sp.zeros(3, 3)
    
    # Calculamos cada componente ~c_{ij}
    for i in range(3):
        for j in range(3):
            # Polinomios de Legendre
            P_i = sp.legendre(i, x)
            P_j = sp.legendre(j, y)
            P_2_x = sp.legendre(2, x)
            P_2_y = sp.legendre(2, y)
            
            # Producto interno: ∫∫ Pᵢ(x)Pⱼ(y) P₂(x)P₂(y) dxdy
            integrando = P_i * P_j * P_2_x * P_2_y
            integral = sp.integrate(sp.integrate(integrando, (x, -1, 1)), (y, -1, 1))
            
            # Normas de los polinomios de Legendre
            norma_i = sp.integrate(P_i**2, (x, -1, 1))
            norma_j = sp.integrate(P_j**2, (y, -1, 1))
            
            # Componente c̃ᵢⱼ = integral / (norma_i * norma_j)
            c_ij = integral / (norma_i * norma_j)
            matriz_componentes[i, j] = c_ij
    
    return matriz_componentes

# Calcular y mostrar la matriz de componentes
matriz_c = componentes_tensor_legendre()

print("d) ", matriz_c)