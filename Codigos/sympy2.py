import sympy
from sympy import *
from sympy.vector import *
R = CoordSys3D("R")
#Considere los siguientes vectores:
 
A = 1*R.i + 2*R.j + 3*R.k
B = 4*R.i + 5*R.j + 6*R.k
C = 3*R.i + 2*R.j + 1*R.k
D = 6*R.i + 5*R.j + 4*R.k

# a) Las siguientes sumas: a+b+c+d, a+b−c−d, a−b+c−d y −a+b−c+d.
suma1 = A+B+C+D
suma2 = A+B-C-D
suma3 = A-B+C-D
suma4 = -A+B-C+D
print("a) suma1= ", suma1)
print("suma2= ", suma2)
print("suma3= ", suma3)
print("suma4= ", suma4)
# b) El ángulo entre los vectores a,b,c,d y los vectores base  e1, e2, e3.
angulo_ai = acos(A.dot(R.i)/(A.magnitude()*R.i.magnitude())).round(3)
angulo_ai = angulo_ai*180/3.14
print("b) El angulo entre A y el eje x es: ",round(angulo_ai,2), "grados")

angulo_aj = acos(A.dot(R.j)/(A.magnitude()*R.j.magnitude())).round(3)
angulo_aj = angulo_aj*180/3.14
print("El angulo entre A y el eje y es: ",round(angulo_aj,2), "grados")

angulo_ak = acos(A.dot(R.k)/(A.magnitude()*R.k.magnitude())).round(3)
angulo_ak = angulo_ak*180/3.14
print("El angulo entre A y el eje z es: ",round(angulo_ak,2), "grados")

angulo_bi = acos(B.dot(R.i)/(B.magnitude()*R.i.magnitude())).round(3)
angulo_bi = angulo_bi*180/3.14
print("El angulo entre B y el eje x es: ",round(angulo_bi,2), "grados")

angulo_bj = acos(B.dot(R.j)/(B.magnitude()*R.j.magnitude())).round(3)
angulo_bj = angulo_bj*180/3.14
print("El angulo entre B y el eje y es: ",round(angulo_bj,2), "grados")

angulo_bk = acos(B.dot(R.k)/(B.magnitude()*R.k.magnitude())).round(3)
angulo_bk = angulo_bk*180/3.14
print("El angulo entre B y el eje z es: ",round(angulo_bk,2), "grados")

angulo_ci = acos(C.dot(R.i)/(C.magnitude()*R.i.magnitude())).round(3)
angulo_ci = angulo_ci*180/3.14
print("El angulo entre C y el eje x es: ",round(angulo_ci,2), "grados")

angulo_cj = acos(C.dot(R.j)/(C.magnitude()*R.j.magnitude())).round(3)
angulo_cj = angulo_cj*180/3.14
print("El angulo entre C y el eje y es: ",round(angulo_cj,2), "grados")

angulo_ck = acos(C.dot(R.k)/(C.magnitude()*R.k.magnitude())).round(3)
angulo_ck = angulo_ck*180/3.14
print("El angulo entre C y el eje z es: ",round(angulo_ck,2), "grados")

angulo_di = acos(D.dot(R.i)/(D.magnitude()*R.i.magnitude())).round(3)
angulo_di = angulo_di*180/3.14
print("El angulo entre D y el eje x es: ",round(angulo_di,2), "grados")

angulo_dj = acos(D.dot(R.j)/(D.magnitude()*R.j.magnitude())).round(3)
angulo_dj = angulo_dj*180/3.14
print("El angulo entre D y el eje y es: ",round(angulo_dj,2), "grados")

angulo_dk = acos(D.dot(R.k)/(D.magnitude()*R.k.magnitude())).round(3)
angulo_dk = angulo_dk*180/3.14
print("El angulo entre D y el eje z es: ",round(angulo_dk,2), "grados")

# c) La magnitud de los vectores a,b,c,d.

magnitud_a = A.magnitude()
magnitud_b = B.magnitude()
magnitud_c = C.magnitude()
magnitud_d = D.magnitude()

print("c) La magnitud de los vectores A,B,C,D son: ", round(float(magnitud_a),2),", ",round(float(magnitud_b),2),", ",round(float(magnitud_c),2),", ",round(float(magnitud_d),2))

# d) El ángulo entre a y b y entre c y d.
angulo_ab = acos(A.dot(B)/(A.magnitude()*B.magnitude())).round(3)
angulo_ab = angulo_ab*180/3.14
print("d) El angulo entre A y B es: ", round(angulo_ab, 2),"grados")
angulo_cd = acos(C.dot(D)/(C.magnitude()*D.magnitude())).round(3)
angulo_cd = angulo_cd*180/3.14
print("El angulo entre C y D es: ", round(angulo_cd, 2), "grados")

# e) La proyección de a sobre b.
proyec_ab = (A.dot(B)/B.magnitude()**2)*A
print("e) La proyeccion de A sobre B es el vector: ", proyec_ab)

# f) Si los vectores a,b,c,d son coplanares

from sympy import Matrix, symbols

def son_coplanares(v1, v2, v3, v4):
    # Creamos una matriz con los 4 vectores como filas
    matriz = Matrix([v1, v2, v3, v4])
    
    # El rango de la matriz debe ser menor que 3 para que sean coplanares
    return matriz.rank() < 3

# Ejemplo de uso:
if __name__ == "__main__":
    # Definimos 4 vectores en R3 (puedes cambiarlos para probar)
    vector1 = (1,2,3)
    vector2 = (4,5,6)
    vector3 = (3,2,1)
    vector4 = (6,5,4)
    
    if son_coplanares(vector1, vector2, vector3, vector4):
        print("f) Los vectores son coplanares.")
    else:
        print("Los vectores NO son coplanares.")

# g) Encuentre (a + b) · (c + d).
suma_ab = A + B
suma_cd = C + D
producto = suma_ab.dot(suma_cd)
print("g) ",producto)

# h) Los productos a × b, b ×c, c×d y los ángulos que estos forman con d.
cruz_ab = A.cross(B)
cruz_bd = B.cross(C)
cruz_cd = C.cross(D)

angulo_1 = acos(cruz_ab.dot(D)/(cruz_ab.magnitude()*D.magnitude())).round(3)
angulo_1 = angulo_1*180/3.14

angulo_2 = acos(cruz_bd.dot(D)/(cruz_bd.magnitude()*D.magnitude())).round(3)
angulo_2 = angulo_2*180/3.14

angulo_3 = acos(cruz_cd.dot(D)/(cruz_cd.magnitude()*D.magnitude())).round(3)
angulo_3= angulo_3*180/3.14


print("h) El angulo entre AxB, BxC, CxD y D son: ", round(angulo_1, 2), round(angulo_2, 2), round(angulo_3, 2), "grados respectivamente")


# i) c · (a × b).

triple = C.dot(A.cross(B))
print("i) ",triple, "son coplanares")