"""Ejercicios de Condicionales: Aquí unos ejercicios simples."""

"""
# Ejercicio 1: Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad = int(input("Escribe tu edad: "))

if edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")

# Ejercicio 2: Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario
# por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la
# variable sin tener en cuenta mayúsculas y minúsculas.
contrasena = input("Escribe la contraseña: ")
pregunta = input("¿Cual es la contraseña?: ")

if pregunta == contrasena:
    print("Acceso concedido.")
else:
    print("Acceso denegado.")

# Ejercicio 3: Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor
# es cero el programa debe mostrar un error.
num1 = int(input("Escribe un numero divisor: "))

if num1 != 0:
    num2 = int(input("Escribe un numero dividendo: "))
    resultado = num1 / num2
    print(f"La division resultante es: {resultado}")
else:
    print("El divisor NO puede ser 0.")

# Ejercicio 4: Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
numero = int(input("Escribe un numero entero: "))

if numero % 2 == 0:
    print("El numero es impar.")
else:
    print("El numero es par.")

# Ejercicio 5: Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o
# superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre
# por pantalla si el usuario tiene que tributar o no.
edad = int(input("Escribe tu edad: "))
ingesos_M = float(input("Escribe tus ingresos mensuales (añade las decimales): "))

if edad > 16 and ingesos_M >= 1000:
    print("Usted debe tributar.")
else:
    print("No debe tributar.")

# Ejercicio 6: Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A
# esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B
# por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que
# le corresponde.
nombre = input("Escribe tu nombre: ")
sexo = input("Escribe tu sexo: ")

primera_letra = nombre[0].upper()  # Obtiene la primera letra y la convierte a mayúscula
segs = sexo.lower()

# condicional simplificada
if 'A' <= primera_letra <= 'M' and segs == 'mujer':
    grupo = 'A'
elif 'N' <= primera_letra <= 'Z' and segs == 'hombre':
    grupo = 'A'
else:
    grupo = 'B'

print(f"Estas en el grupo: {grupo}.")

# Ejercicio 7: Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Renta	                Tipo impositivo
# Menos de 10000€	        5%
# Entre 10000€ y 20000€	    15%
# Entre 20000€ y 35000€	    20%
# Entre 35000€ y 60000€	    30%
# Más de 60000€	            45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
renta = float(input("Escribe tu renta anual: "))

if renta < 10000:
    print(f"Tu impositivo es de 5%. Por lo que tienes que pagar: ${renta*0.05}")
elif renta < 20000:
    print(f"Tu impositivo es de 15%. Por lo que tienes que pagar: ${renta*0.15}")
elif renta < 35000:
    print(f"Tu impositivo es de 20%. Por lo que tienes que pagar: ${renta*0.20}")
elif renta < 60000:
    print(f"Tu impositivo es de 30%. Por lo que tienes que pagar: ${renta*0.30}")
else:
    print(f"Tu impositivo es de 45%. Por lo que tienes que pagar: ${renta*0.45}")

# Ejercicio 8: En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden
# obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que
# pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras
# mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de
# dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de
# dinero que recibirá el usuario.

nivel = float(input("Escribe tu nivel de rendimiento: "))

if nivel == 0.0:
    print(f"Tu nivel es inaceptable, por lo que no obtienes bono.")
elif nivel == 0.4:
    print(f"Tu nivel es Aceptable, obtienes un bono de: ${nivel * 2400}.")
elif nivel >= 0.6:
    print(f"Tu nivel es Meritorio, obtienes un bono de: ${nivel * 2400}.")
else:
    print("Tu nivel no esta en el rango de bonos.")

# Ejercicio 9: Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular
# de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad
# del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre
# 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
edad = int(input("Escribe tu edad: "))

if edad < 4:
    print("Su entrada es gratis.")
elif edad <= 18:
    print("Debes pagar $5.")
else:
    print("Debes pagar $10.")

# Ejercicio 10: La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes
# para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le
# muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la
# mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
# vegetariana o no y todos los ingredientes que lleva.

print("\tPizzeria Los Papus")
pizza = int(input("Estas son las pizzas que ofrecemos: \n1.-Vegetariana. \n2.-No vegetariana \nEscoge el tipo de pizza que deseas: "))
if pizza == 1:
    eleccion = int(input("\nIngredientes para pizza vegetariana: \n1.- Pimiento \n2.- Tofu \n Escoge el ingrediente: "))
    if eleccion == 1:
        print(f"Tu pizza tendra: Tomate, Mozzarella y Pimiento.")
    elif eleccion == 2:
        print(f"Tu pizza tendra: Tomate, Mozzarella y Tofu.")
    else:
        print("La opcion no esta en el rango.")
elif pizza == 2:
    eleccion = int(input("\nIngredientes para pizza NO vegetariana: \n1.- Peperoni \n2.- Jamón \n3.- Salmón \n Escoge el ingrediente: "))
    if eleccion == 1:
        print(f"Tu pizza tendra: Tomate, Mozzarella y Peperoni.")
    elif eleccion == 2:
        print(f"Tu pizza tendra: Tomate, Mozzarella y Jamón.")
    elif eleccion == 3:
        print(f"Tu pizza tendra: Tomate, Mozzarella y Salmón.")
    else:
        print("La opcion no esta en el rango.")
else:
    print("La opcion no esta en el rango.")
"""
