"""Aquí estaran unos ejercicios simples sobre tipos de datos."""

"""
# Ejercicio 1: Escribe por pantalla un hola mundo.
print("Hola Mundo")

# Ejercicio 2: Escribe un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el
# contenido de la variable.
hola = "¡Hola Mundo!"
print(hola)

# Ejercicio 3: Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo
# introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
nombre = input("Escribe tu nombre: ")
print(f"Hola {nombre}")

# Ejercicio 4: Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética
# (3+2/2*5)^2.
operacion = ((3+2)/(2*5))**2
print(f"Resultado: {operacion}")

# Ejercicio 5: Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.
horas = int(input("Escribe las horas trabajadas: "))
paga = float(input("Escribe cuanto te pagan por hora: "))

print("Tu paga sera de: " + str(horas*paga))

# Ejercicio 6: Escribir un programa que lea un entero positivo n, introducido por el usuario y después muestre en pantalla
# la suma de todos los enteros desde 1 hasta n. La suma de los primeros n enteros positivos puede ser calculada de la
# siguiente forma: suma = n(n+1)/2
numero = int(input("Escribe un numero: "))
print(f"La suma de los numeros hasta {numero}, es igual a: " + str(numero*(numero+1)/2))

# Ejercicio 7: Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de
# masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde
# <imc> es el índice de masa corporal calculado redondeado con dos decimales
peso = float(input("Escribe tu peso en KG: "))
estatura = float(input("Escribe tu altura en metros: "))

print(f"De acuerdo a tu peso: {peso} y tu altura: {estatura}. Tu indice de masa corporal es: " + str(round(peso/estatura**2, 2)))

# Ejercicio 8: Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da
# un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el
# cociente y el resto de la división entera respectivamente.
num1 = int(input("Escribe un numero entero: "))
num2 = int(input("Escribe otro numero entero: "))

print(f"La división entre {num1} y {num2}, da un cociente de: {str(num1//num2)} y el resto es: {str(num1%num2)}")

# Ejecicio 9: Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de
# años, y muestre por pantalla el capital obtenido en la inversión. 

inversion = float(input("Escribe la cantidad a invertir: "))
int_anual = float(input("Escribe el interes anual: "))
años = int(input("Escribe la cantidad de años a invertir: "))

print(f"El interes compuesto de la inversion es: {str(round(inversion*(int_anual/100+1)**años, 2))}")

# Ejercicio 10: Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por
# correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y
# muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea
# el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
payaso = 0.112
muñeca = 0.75
venta_payaso = int(input("Escribe la cantidad de payasos vendidos: "))
venta_muñecas = int(input("Escribe la cantidad de muñecas vendidas: "))

print(f"El peso del paquete que sera enviado, es de: {str((payaso*venta_payaso)+(muñeca*venta_muñecas))} kg.")

# Ejercicio 11: Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos
# ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de
# ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
# introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el
# primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
ahorros = float(input("Escribe la cantidad de ahorros que tienes: "))
interes = 0.04
balance1 = ahorros*(interes+1)
balance2 = balance1*(interes+1)
balance3 = balance2*(interes+1)

print(f"La cantidad de ahorro en el año 1 es: {str(round(balance1, 2))}, en el año 2 es de: {str(round(balance2, 2))}, y en el año 3 es de: {str(round(balance3, 2))}")
"""

# Ejercicio 12: Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe
# mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
pan = 3.49
barras_viejas = int(input("Escribe la cantidad de barras que no son del dia que se vendieron: "))
print(f"El precio de una barra fresca es de: {pan} euros. Por comprar barras de pan que NO son del dia, se le aplica un "
      f"descuento del 60%. \nUsted compro {str(barras_viejas)} de barras que NO son del dia, por lo que tendra que pagar: "
      f"{str(round((pan*barras_viejas)*0.40, 2))} euros.")
