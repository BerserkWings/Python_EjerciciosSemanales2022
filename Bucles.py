"""Ejercicios de Bucles: Aquí estarán unos ejercicios simples de bucles"""

"""
# Ejercicio 1: Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = input("Escribe una palabra: ")

for i in range(10):
    print(palabra)

# Ejercicio 2: Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha
# cumplido (desde 1 hasta su edad).
edad = int(input("Escribe tu edad: "))

for i in range(1, 1+edad):
    print(f"Has cumplido: {i} años.")

# Ejercicio 3: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los
# números impares desde 1 hasta ese número separados por comas.
numero = int(input("Escribe un numero entero: "))
print("Los impares son: ")
for i in range(1,numero+1,2):
    print(i, end=',')

# Ejercicio 4: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás
# desde ese número hasta cero separados por comas.
numero = int(input("Escribe un numero: "))

for i in range(numero, -1, -1):
    print(i, end=',')

# Ejercicio 5: Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de
# años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
inversion = float(input("Escribe la cantidad a invertir: "))
interes = float(input("Escribe el interes anual: "))
años = int(input("Escribe los años a invertir: "))

for i in range(años):
    inversion*=1 + interes/100
    print(f"Año: {i}, Capital: {str(round(inversion,2))}")

# Ejercicio 6: Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo
# como el de más abajo, de altura el número introducido.
#
# *
# **
# ***
# ****
# *****
numero = int(input("Escribe un numero: "))

#for i in range(1,numero+1):
 #   print(i*'*')

for i in range(1,numero):
    espacios = ' ' * (numero-i)
    asteriscos = '*' * i
    print(espacios+asteriscos+asteriscos[::-1])

# Ejercicio 7: Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
sum = 0
for i in range(1, 11):
    sum += 1
    print()
    for j in range(1, 11):
        print(f"Tabla: {sum}, es igual a :{j*i}")

# Ejercicio 8: Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo
# como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1
numero = int(input("Escribe un numero entero: "))
for i in range(1, numero+1, 2):
    for j in range(i, 0, -2):
        print(j, end=' ')
    print()
    
# Ejercicio 9: Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario
# por la contraseña hasta que introduzca la contraseña correcta.

contra = "contraseña"
passwd = ""
while passwd != contra:
    passwd = input("Escribe la contraseña: ")
print("Acceso concedido...")

# Forma Brgas
contra = input("Escribe una contraseña: ")
buck = 0
while buck != 1:
    passwd = input("Escribe la contraseña que escribiste: ")
    if passwd == contra:
        print("Acceso concedido...")
        buck = 1
    else:
        print("La contraseña es incorrecta.")

# Ejercicio 10: Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número
# primo o no.

numero = int(input("Escribe un numero entero: "))
if numero < 2:
    print(f"El numero {numero} NO es primo.")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"El numero {numero} NO es primo.")
            break
    print(f"El numero {numero} es primo.")

# Ejercicio 11: Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras
# de la palabra introducida empezando por la última.

palabra = input("Escribe una palabra: ")
for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])

# Ejercicio 12: Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla
# el número de veces que aparece la letra en la frase.
frase = input("Escribe una frase: ")
letra = input("Escribe una letra: ")
contador = 0

for i in frase:
    if i == letra:
        contador += 1
print(f"La frase: {frase}, tiene la letra {letra} {contador} veces.")

# Ejercicio 13: Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario
# escriba “salir” que terminará.
print("Escibre 'salir' para salir.\n")

while True:
    eco = input("Escribe lo que quieras que se vea en el eco: ")
    if eco == 'salir':
        break
    print(eco)
"""











