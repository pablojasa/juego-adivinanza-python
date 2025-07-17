
#----------------------------------------
# ESTRUCTURAS DE CONTROL - CONDICIONALES
#----------------------------------------

# Permiten  ejecutar diferentes bloques de codigo dependiendo de si se cumplen ciertas condiciones o no.

# if condicion_1:
    # Codigo a ejecutar si la condicion_1 es verdadera

# elif condicion_2:
    # Codigo a ejecutar si la condicion_2 es verdadera

# else:
    # Codigo a ejecutar si ninguna de las condiciones anteriores es verdadera

#----------------------------------------
# CONDICIONALES TERNARIAS
#----------------------------------------

# Son una forma concisa de expresar una estructura condicional en una sola linea
# Se utilzan principalmente para asignar a una variable en funcion de una condicion.

# valor_sin_condicion_verdadera if condicion else valor_si_condicion_falsa

# Ejemplo:

# x = 10
# resultado = "positivo" if x > 0 else "negativo"

# print (resultado)

# ----------------
# BUCLES (LOOPS)
# ----------------


# BUCLE WHILE

# while condicion:
    # Codigo a ejecutar mientras la condicion sea verdadera.

#BUCLE FOR

# for indice in range(cantidad):
    # Codigo a ejecutar en cada iteracion
    # Permite recorrer una estructura


# --------------------------
# MANEJO DE EXCEPCIONES
# --------------------------

# Las estructuras de control de manejo de excepciones en Python permiten manejar errores y excepciones que pueden ocurrir durante la ejecucionn de un programa.

# try:
#     # Codigo que puede generar una excepcion
# except TipoDeExcepcion as nombre_variable:
#     # Codigo para manejar la excepcion
# finally:
#     # Codigo que siempre se ejecuta, OPCIONAL


# --------------------------------------
# PALABRAS CLAVE PARA CONTROL DE FLUJO
# --------------------------------------

# Forman parte del conjunto de herramientas que Python proporciona para controlar el flujo de ejecucion y la logica del programa.

# BREAK
# termina la ejecucion del bloque actual y continua con la siguiente instruccion fuera del bucle

# for i in range(5):
    # if i == 3:
        # break
    # print(i)   se espera: 0,1,2


# CONTINUE
# salta a la siguiente iteracion del bucle omitiendo el resto del codigo dentro del bucle para la iteracion actual.

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)


# PASS
#  se utiliza como marcador de posicion

# x = 10
# if x > 5:
#     pass
# else:
#     print("x es menor o igual a 5")


# ---------------------------
# IF, ELIF, ELSE
# ---------------------------
# Estructuras de control condicionales

# x = 10

# if x > 0:
#     print("x es un numero positivo")
# elif x < 0:
#     print("x es un numero negativo")
# else:
#     print("x es igual a 0")

#----------------------

# Queremos viajar internacionalmente

# visa = False
# pasaporte = True

# if visa and pasaporte:
#     print("Puedes ingresar al pais de destino")

# elif pasaporte and not visa:
#     print("Puedes ingresar solo a los paises que no requieren Visa")

# else:
#     print("Debes conseguir la documentacion antes de viajar")

# ----------------------------

# edad = 40

# if edad < 18 or edad > 60:
#     if edad < 18:
#         print ("No tienes edad suficiente para entrar a la disco")
#     else:
#         print("Por una cuestion de seguridad, no se permite el ingreso a mayores de 60")
# elif edad >= 18 and edad <= 60:
#     print("Puedes ingresar a la disco")


from ast import For, While


# -----------------------
# ESTRUCTURAS DE CONTROL: BUCLES
# WHILE (mientras..... se cumpla una condicion)
# -----------------------


# contador = 0

# while contador < 5:
#     print("El contador es: ", contador)
#     contador += 1

# print(contador)


# # NO ES LO MISMO


# contador = 0

# while contador < 5:
#     contador += 1
#     print("El contador es: ", contador)

# print(contador)


# ----------------------------

# contador = 0
# limite = 5
# sumatoria = 0

# while contador <= limite:
#     sumatoria += contador
#     contador += 1

# print("La suma de los numeros hasta", limite, "es:", sumatoria)



# ------------------------
# Estructura de control
# BUCLE FOR
# ------------------------

# Permite recorrer un rango

# for i in range(5):
#     print(i)

# Rta:
# 0
# 1
# 2
# 3
# 4

# for i in range(1,11):
#      print(i)

# Rta:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# OJO: el primer numero del rango esta incluido, EL ULTIMO NO.

# for i in range(0,11,2):   #salta de dos en dos
#     print(i)

# Rta:
# 0
# 2
# 4
# 6
# 8
# 10


# for i in range(0,9,2):   #salta de cuatro en cuatro
#     if i == 2:
#         print("Pasó por el numero 2")
#     print(i)

# Rta:
# 0
# Pasó por el numero 2
# 2
# 4
# 6
# 8


# for i in range(0,9,2):   #salta de cuatro en cuatro
#     if i == 2:
#         print("Pasó por el numero 2")
#     else:
#         print("No es numero 2, es el numero", i)

# Rta:
# No es numero 2, es el numero 0
# Pasó por el numero 2
# No es numero 2, es el numero 4
# No es numero 2, es el numero 6
# No es numero 2, es el numero 8


# --------------------------------------
# TRY EXCEPT FINALLY
# Manejo de errores
# --------------------------------------

#Manejo de la division por cero (falla)

# a = 10
# b = 0

# c = a/b

# print(c)

# Rta:
# ZeroDivisionError: division by zero

# a = 10
# b = 0
# try:
#     resultado = a/b
#     print(resultado)

# except ZeroDivisionError:
#     print("No se puede dividir por cero")

#     print("Hola, mi nombre es Pablo")

# Rta:
# No se puede dividir por cero
# Hola, mi nombre es Pablo

# no se rompe el codigo y continua ejecutando

# a = 10
# b = 0

# try:
#     resultado = a/b
#     print(resultado)

# except ZeroDivisionError:
#     print("No se puede dividir por cero")
# finally:
#     resultado = 0

# print(resultado)

# Rta:
# No se puede dividir por cero
# 0


# a = 10
# b = 5

# try: #Intenta algo
#     resultado = a/b
#     print(resultado)

# except ZeroDivisionError: #Si tiene un error lo maneja
#     print("No se puede dividir por cero")
# finally: #se ejecuta siempre
#     resultado = 0

# print(resultado)

# Rta:
# 2.0       #la division arroja un flotante
# 0         #luego ejecuta el finally




# -------------------------------
# BREAK CONTINUE PASS
# Palabras claves dentro de las estructuras de control
# --------------------------------

# BREAK

# contador = 0

# while contador < 10:
#     print(contador)
#     if contador == 5:
#         break
#     contador += 1

# Rta:
# 0
# 1
# 2
# 3
# 4
# 5



# contador = 10
# prohibido = 23

# while contador < 25:
#     print(contador)
#     if contador == prohibido:
#         break
#     contador += 1

# Rta:
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23        # El contador llega hasta 23 y el BREAK lo interrumpe


# contador = 0

# while contador < 5:
#     print(contador)
#     if contador == 3:
#         continue
#     contador += 1

#OJO: porque el CONTINUE hace que se salte lo que queda de codigo, con lo cual no va a sumar el +=1

# SE PUEDE CORTAR CON CTRL + C


# contador = 0

# while contador < 5:
#     print(contador)
#     contador += 1
#     if contador == 3:
#         continue
#     print("Imprimir por cada vuelta")

# print(contador)

# Rta:
# 0
# Imprimir por cada vuelta
# 1
# Imprimir por cada vuelta
# 2                           #Aca salto el codigo
# 3
# Imprimir por cada vuelta
# 4
# Imprimir por cada vuelta
# 5



# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# Rta:
# 1
# 3
# 5
# 7
# 9   #SALTA EL PRINT PORQUE ESTA DENTRO DEL BUCLE CUANDO EL DIVISIBLE POR 2



# PASS


# edad = 18
# if edad > 18:
#     print("Puedes ingresar a esta institucion")
# elif edad == 18:
#     pass     #permite que ese bloque de codigo se ignore
# else:
#     print("No tienes edad suficiente para entrar aqui")
