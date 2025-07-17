
# OPERADORES

# Son simbolos o conjunto de simbolos que realizan una operacion especifica en uno o mas operando.

# TIPOS DE OPERADORES

    # ARITMETICOS
    # DE COMPARACION
    # LOGICOS
    # DE ASIGNACION
    # DE PERTENENCIA
    # DE IDENTIDAD


# OPERADORES ARIRMETICOS

"""
a = 5
b = 4

# + para sumar
# - para restar
# * para multiplicar
# / para dividir
# // para dividir entero (floor division)
# % modulo (resto / modulus)
# ** exponenciacion

c = a // b
d = a % b

print(c)
print (type(c))
print(d)

"""

# OPERADORES DE ASIGNACION

# = ASIGNACION / Puede asignar un texto o un valor a una variable


# 

"""
x = 10
sumatorio = 3

# 10
x += sumatorio # 13
x += sumatorio # 16
x += sumatorio # 19
x += sumatorio # 22

print(x)


x = 10
aRestar = 2

# 10
x -= aRestar #8
x -= aRestar #6
x -= aRestar #4
x -= aRestar #2

print(x)


x = 10
aMultiplicar = 2

#10
x *= aMultiplicar #20
x *= aMultiplicar #40
x *= aMultiplicar #80
x *= aMultiplicar #160

print (x)



x = 400
divisor = 2

#400

x /= divisor #200
x /= divisor #100
x /= divisor #50
x /= divisor #25

print (x)  # el operador de division devuelve un float
print (int(x))



x = 100
divisor = 2

#100
x /= divisor #50
x /= divisor #25
x /= divisor #12.5
x /= divisor #6.25

print (x)  # el operador de division devuelve un float


x = 100
divisor = 2

#100
x //= divisor #50
x //= divisor #25
x //= divisor #12
x //= divisor #6

print (x)  # puede perder precision en multiples divisiones


x = 2
aExponer = 2

# 2

x **= aExponer # 4
x **= aExponer # 16
x **= aExponer # 256
x **= aExponer # 65536

print (x) 

"""
# -----------------------------
# OPERADORES DE COMPARACION
# -------------------------------

# NO ES LO MISMO USAR EL = PARA ASIGNAR QUE DOS = (==)

# x = 5
# y = 5

# # print(x == y) # True

# print(x != y) # False
# # ! es la negación (ampliaremos)
# # != nos sirve para comparar diferencia

# x = 4
# y = 5

# print(x < y) # True
# print(x > y) # False




# x = 5
# y = 5

# print(x <= y) # True
# print(x >= y) # True

# > Mayor que
# < Menor queue
# <= Menor o is_regular
# >= Mayor o is_regular


# ----------------------------
# OPERADORES LOGICOS
# ------------------------------

# and nos va a devolver true si ambas afirmaciones son verdaderas
# or nos va a devolver true si algunas de las dos afirmaciones es verdaderas
# not nos devolvera el opuesto al valor que siga



# x = 5
# booleano = x > 3 and x < 10

# print (booleano) # True

#----------------------------

# x = 15
# booleano = x > 3 and x < 10

# print (booleano) # False

# ------------------------------


# x = 15
# booleano = x > 3 or x < 10

# print (booleano) # True

#---------------------------------

# x = 0 
# booleano = x >= 0 or x!= 10

# print (booleano) # True

# ---------------------------------

# x = 0
# booleano = x > 0 and x < -100

# print(booleano) # False


# -------------------------------

# x = 0
# booleano = not x == 0

# print(booleano) # False


# x = 50
# booleano = not x == 0

# print(booleano) # True


# x = 0
# y = 5

# a = x > y # False
# b = y > x # True

# booleano = not (a and b) # True

# print(booleano)



# x = 0
# y = 5

# a = x < y # True
# b = y > x # True

# booleano = not (a and b) # False

# print(booleano)





# --------------------------
# OPERADORES DE IDENTIDAD
# --------------------------

# is
# is not


# a = 5
# b = 5

# booleano = a is b  # True
# tambien funciona usando el ==

# print(booleano)

# a = "Esto es un texto"
# b = "Esto es un texto"

# booleano = a is b #True
# booleano1 = a == b #True

# print (booleano)
# print (booleano1)



# --------------------------
# OPERADORES DE PERTENENCIA
# --------------------------



from ast import Pass


texto = "En este texto pondremos algunas tecnologias: Python, R, Django y TensorFlow"

# print ("Django" in texto) # True
# print ("Django" not in texto) # Falso
# print ("django" in texto) # Falso. Reconoce la falta de mayuscula en la inicial

# Solucionar el Case Sensitive

# textominuscula = texto.lower()
# aBuscar = "     TENsORFLoW     ".strip().lower()

# print(aBuscar in textominuscula) #True
# print(aBuscar not in textominuscula) #False



