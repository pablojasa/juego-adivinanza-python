# SINTAXIS DE PYTHON

# Reglas que se deben seguir al escribir para que sea valido y pueda ser interpretado correctamente.

#INDENTACION:

# La indentacion es el 'espacio en blanco' llamado tabulacion o sangria al comienzo de una linea de codigo

# El scope / alcance de una estructura no se delimitara por llaves como otros lenguajes sino a traves de la indentacion

"""
#------------------------ Esto es una estructura
for i in range(S):
    print(i)
#------------------------ Esta es otra estructura
print(i)
"""

# VARIABLES

# Contenedores que almacenan datos que pueden cambiar durante la ejecucion de un programa.
# Cada variable tiene un nombre unico y un valor asociado
# Para poder asignarle ese valor se utiliza el operador =

"""
x = 5
nombre = "Juan"
y = str(x) #casteo (cambiar de tipo de formato)

print(x)
print(nombre)
print(y)

# VALIDO: Si comienza con una letra y sin caracteres epeciales
mivariable = "Texto"

# VALIDO: Si comienza con una letra y con guiones bajos intermedios
mi_variable = "Texto"

# VALIDO: Podemos comenzar con _
_mi_variable = "Texto"

# VALIDO: camelCase que se utilizan mayusculas al comenzar cada palabra, salvo la primera
miVariable = "Texto"

# VALIDO: puede comenzar y ser todo mayuscula
MIVARIBLE = "Texto"

# VALIDO: podemos utilizar numeros pero no al comienzo
mivariable1 = "Texto"

# NO VALIDO: comenzar con numeros
2mivarible = "Texto"

# NO VALIDO: usar - guion medio
mi-variable = "Texto"

# NO VALIDO: usar espacios
mi variable = "Texto"

#NO VALIDO: usar simbolo $
$mivariable = "Texto"
"""


# TIPOS DE DATOS

"""
#----------------
# TEXTO:
#----------------
# - str (cadena de caracteres)
texto = "Cadena de caracteres"

#----------------
# NUMERICOS
#----------------

# - int (numero entero, sin decimal, puede ser negativo)
numero_entero = 10

# - float (flotante)
numero_flotante = 3.14

# - complex (complejo, numero real e imaginario)
numero_complejo = 2 + 3j

#----------------
# SECUENCIA
#----------------

# - list (lista) [coleccion ordenada y mutable]
lista = [1,2,3,4]

# - tuple (tupla) [coleccion ordenada e inmutable]
tupla = (1,2,3)

# - range (rango) [secuencia inmutable de numeros]
rango = range(0, 10)

#----------------
# MAPPING TYPE (MAPEO)
#----------------

# - dict (diccionario) [coleccion no ordenada de pares clave-valor]
# recomendado indentar cada par
diccionario = {
    "nombre": "Pablo", 
    "edad": 41
    "direccion": "Av. Siempre Viva 742"
}

#----------------
# SET TYPES (CONJUNTO)
#----------------

# - set (conjunto) [coleccion no ordenada y mutable de elementos UNICOS (no permite repetir)]

conjunto = {1,2,3,4}

# frozenset (conjunto inmutable) [conjunto inmutable]
conjunto_inmutable = frozenset({1,2,3,4})

#----------------
# BOOLEAN TYPES (BOOLEANO)
#----------------

# - boolean (puede ser verdadero o falso)

booleano = True
booleano2 = False

#----------------
# BINARY TYPES (BINARIOS)
#----------------

# - bytes [Representa una secuencia inmutable de bytes]
bytes_data = b"datos"

# - bytearray (array de bytes) [Representa una secuencia mutable de bytes]

bytearray_data = bytearray(b"datos")

# - memoryview (vista de memoria) [Permite acceder a la memoria de objetos de bytes sin hacer una copia]
memoria = memoryview(b"datos")

#----------------
# NONE/NULL (NULO)
#----------------

# NoneType (nulo) [Representa la ausencia de valor o la no definicion]
nulo = None
"""

# CASTEO (cambiar el tipo de dato de uno a otro)

"""
# Texto (str)
variable1 = "Texto"
variable2 = "123456"
variable3 = "Texto123"

# Numericas (int, float, complex)
variable4 = 10
variable5 = 2.5
variable6 = 1j


print(type(variable1)) # <class 'str'>
print(type(variable2)) # <class 'str'>
print(type(variable3)) # <class 'str'>
print(type(variable4)) # <class 'int'>
print(type(variable5)) # <class 'float'>
print(type(variable6)) # <class 'complex'>


# Casteo de str a int
variableCasteada = int(variable2)

# Casteo de int a str
variableCasteada2 = str(variable4)

print(type(variableCasteada)) # <class 'int'>
print(type(variableCasteada2)) # <class 'str'>


lista = ["manzana", "pera", "naranja"]
x = list(("manzana", "pera", "naranja"))

print(type(lista)) # <class 'list'>
print(type(x)) #<class 'list'>

# ¿Como se castea? (Cambiar de tipo de dato) tipoDeDato("el dato original")
# Con type podemos saber qué tipo de datos es el que estamos manejando
"""

# TIPO DE DATOS NUMERICOS

"""
x = 1 # int
y = 2.8 # float
z = 5+2j # complex

print(type(x))
print(type(y))
print(type(z))


x = 5

y = float(x)

print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>

x = 5.5

y = int(x)

print(x) # 5.5
print(type(x)) # <class 'float'>

print (y) # 5
print(type(y)) # <class 'int'>

# Un numero complex no puede ser casteado a int o float

"""

# RANDOM

"""
import random

≈x = random.randrange(1,10) #no esta incluido el 10

print(x)



x = random.random()

print(x) #da un valor entre 0 y 1
print(type(x)) # <class 'float'>

x = random.randint(1,10) # rango que incluye al 10

print(x)
print(type(x)) # <class 'int'>
"""

# CADENA DE CARACTERES
"""

txt = 'Hola Mundo'
print(txt)

"""""


txt1 = """
Hola Mundo
print(txt1) #Las comillas triples permiten hacer saltos de linea.


print(txt[0]) # El indice indica el lugar o posicion donde esta un elemento en una estructura.

print(txt[1])
print(txt[2])
print(txt[3])
print(txt[4])
    

txt = "Hola Mundo"

print(len(txt)) #Cuenta cantidad de caracteres.

#---------------------

int = len(txt)

print(int) #Los espacios tambien cuentan como caracteres


txt = "En este texto les explicare acerca de las cadenas de caracteres, en ingles llamadas STRING"

print("ingles" in txt) #Ojo, porque reconoce tildes y mayusculas. Es CASE SENSITIVE.

print("ingles" not in txt)
"""

#txt = "Seguimos trabajando con Strings"

# print(txt[8:18]) # No llega a tomar el carater ubicado en el espacio 18

#Slicing ponemos desde un indice hasta un indice NO incluido

#print(txt[:8]) #Dejando vacio el primer lugar, toma desde el comienzo del string

#print(txt[23:]) Dejando vacio el final, toma desde el lugar de inicio hasta el final

#print(txt[-7:]) Lectura inversa de la posicion 7 contando desde el final.

#print(txt[-11:-1])

#-----------------------------------

#txt = "CUANDO ESCRIBO EN MAYUSCULA TODOS PIENSAN QUE ESTOY GRITANDO"

#print(txt.lower()) Pasa el string a Lower Case (minuscula)

#minuscula =txt.lower()

#print(minuscula)

#-----------------------------------

#txt = "este texto es tan importante que si lo pongo en minusculas nadie le presta atencion"

#mayusculas = txt.upper()

#print(mayusculas)

#-----------------------------------

#vtxt = "      Uy! Me deje algunos espacios antes y desppues de este texto!     "

#vextoimportante = "clave "

#vtxtcorregido = txt.strip()

#vtxtcorregido2 = textoimportante.strip()

# print(txtcorregido)
# print(txtcorregido2)

#-----------------------------------
"""
a = "Hola"

b = "Mundo"

# c = a + b

# print(c) # HolaMundo

c = a + " " + b

print(c) # Hola Mundo

txt = "El contenido de este curso va a durar: "
horas = 10

concatenado = txt + horas

print(concatenado) # NO DA (concatenado = txt + horas)

# hay que castearlo


txt = "El contenido de este curso va a durar: "
horas = 10

concatenado = txt + str(horas) + " horas"

print(concatenado) # El contenido de este curso va a durar: 10 horas



horas = 10
txt = "El contenido de este curso va a durar: {} horas"

print(txt.format(horas))




horas = 10
clases = 60
# txt = "El contenido de este curso va a durar: {} horas y tendra {} clases"

# print(txt.format(horas, clases))

txt = "El contenido de este curso va a durar: {1} horas y tendra {0} clases"

print(txt.format(clases, horas))

"""


# --------------------------------
# METODOS DE CADENA DE CARACTERES
# --------------------------------
"""
txt= "este texto está todo en minúscula este"

print(txt.capitalize()) #[pone mayuscula en la primer letra del string]

print(txt.title()) #convierte el primer caracter de cada palabra en mayuscula

word = "centrado"

print(word.center(20)) #centra el string en la cantidad de espacio determinado

print(txt.count("este")) # devuelve el nro de veces que aparece un valor espacificado en el string


txt = "Las manzanas son mi fruta favorita ¿tienes alguna manzana? Si, 3 manzanas"

# print(txt.endswith("manzanas")) # Devuelve verdadero si la cadena termina con el valor especificado

# print(txt.find("manzanas")) # Busca un valor especificado en la cadena y devuelve la posicion donde se encontro

numeros = "123456789"

# print(numeros.isdigit()) # Devuelve verdadero si todos los caracteres de la cadena son digitos.

# print(numeros.isdecimal()) # Devuelve verdadero si todos los caracteres de la cadena son decimales (no confundir con float)

print(txt.islower())

"""


