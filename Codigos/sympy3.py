from sympy import symbols, cos, sin, pi, integrate
from sympy.vector import CoordSys3D
R = CoordSys3D("R")

#Definimos las componentes del campo vectorial
F_x = -R.y / (R.x**2 + R.y**2)
F_y = R.x / (R.x**2 + R.y**2)

#Definimos el campo vectorial 
F = F_x * R.i + F_y * R.j

#Parametrizamos el circulo 
theta = symbols("theta")
x = cos(theta)
y = sin(theta)

#Sustituimos en el campo las variables nuevas
F_new = F.subs({R.x: x, R.y:y})

#Calculamos el diferencial de desplazamiento
dr_theta = -sin(theta)*R.i + cos(theta)*R.j

# Expresamos el trabajo 
integrando = F_new.dot(dr_theta)

integrando_simplificado = integrando.simplify()  #Simplificamos el trabajo 
print("El producto punto es: ", integrando_simplificado)

# Calcular el trabajo para los dos casos
# Trabajo = - int(F · dR)
W_a = -integrate(integrando_simplificado, (theta, 0, pi))
W_b = -integrate(integrando_simplificado, (theta, 0, -pi))

print("Trabajo en el caso (a) [0 a π]:", W_a)
print("Trabajo en el caso (b) [0 a -π]:", W_b)