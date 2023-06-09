"""Ejercicios de Cadenas/Strings, estos son algunos ejercicios simples."""

"""
# Ejercicio 1: Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por
# pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
nombre = input("Escribe tu nombre: ")
numero = int(input("Escribe un numero: "))
print(f"Tu nombre es: {nombre}.\n" + (nombre+'\n')*numero)

# Ejercicio 2: Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el
# nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y
# otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre
# combinando mayúsculas y minúsculas como quiera.
nombre = input("Escribe tu nombre: ")
print("Tu nombre es: \n" + nombre.upper() + '\n' + nombre.lower() + '\n' + nombre.title())

# Ejercicio 3: Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo
# introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n>
# es el número de letras que tienen el nombre.
nombre = input("Escribe tu nombre: ")
print(f"Tu nombre es: {nombre.upper()} y tiene {str(len(nombre))} letras.")

# Ejercicio 4: Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el
# código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que
# pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y
# la extensión.
numero = input("Escribe un numero de celular (ej. 34-913724710-56): ")
print(f"El numero celular sin prefijo ni extension es: {numero[3:12]}")

# Ejercicio 5: Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla
# la frase invertida.
frase = input("Escribe una frase a invertir: ")
print(f"La frase invertida es: {frase[::-1]}")

# Ejercicio 6: Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después
# muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
frase = input("Escribe una frase: ")
vocal = input("Introduce una Vocal: ")
print(f"Remarcando la vocal en la frase: {frase.replace(vocal, vocal.upper())}")

# Ejercicio 7: Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla
# otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
correo = input("Escribe tu correo: ")
print(f"Tu nuevo correo es: {correo[:correo.find('@')] + '@ceu.es'}")

# Ejercicio 8: Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y
# muestre por pantalla el número de euros y el número de céntimos del precio introducido.
precio = input("Escribe el precio del producto, incluye las decimales: ")
print(f"Separando los enteros de los decimales, son: {precio[:precio.find('.')]} euros, con {precio[precio.find('.')+1:]} decimas.")

# Ejercicio 9: Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra
# por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes
# se introduzcan con un solo carácter.
fecha = input("Escribe tu fecha de nacimiento en formato dd/mm/aaaa: ")
print(f"Tu naciste el dia: {fecha[:fecha.find('/')]}, del mes: {fecha[fecha.find('/')+1:fecha.find('/')+3]}, del año: {fecha[6:10]}")

# Ejercicio 10: Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por
# comas, y muestre por pantalla cada uno de los productos en una línea distinta.
productos = input("Escribe los productos que vas a comprar, separalos por comas: ")
print(f"Los productos son: \n " + productos.replace(',', '\n'))
"""
