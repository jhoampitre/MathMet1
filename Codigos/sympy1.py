#Dado que para un triangulo de densidad uniforme su centro de masas coincide con el centroide geometrico, calculamos el centro de masas donde los vertices son las masas y son iguales entre ellas.
from sympy import symbols, Matrix, Eq, simplify, N
#Definimos una funcion que debe terner como entrada el punto de los vertices y el numero de demcimales ademas
def centro_de_masa(vertices, masas=None, decimales=2):
    if masas is None:
        centro_x = sum(v[0] for v in vertices) / 3
        centro_y = sum(v[1] for v in vertices) / 3
        centro = Matrix([centro_x, centro_y])
        return centro.applyfunc(lambda x: N(x, decimales))
#Aca simplementre hallamos el punto promedio de las coordenadas de los vertices "x" y "y"
if __name__ == "__main__":
    A = Matrix([1,3]) #Estos datos pueden ser reemplazados por otros vertices que querramos
    B = Matrix([2,2])
    C = Matrix([3,1])

    vertices = [A,B,C]
    centroide = centro_de_masa(vertices, decimales=2)
    print("El Centroide del triangulo se encuentra en el punto :", tuple(float(N(x,2))for x in centroide))
