# Variables
# Tipos de datos

# Nombre de la variable = valor
# variable deber tipo snake case
# ejemplo: nombre_de_la_variable = valor

first_name = "Juan Alfonso" # String
last_name = 'Carrasco Mendez'
full_name = first_name + ' ' + last_name

print(first_name) # Muestra en consola el valor de la variable
print(last_name)
print(full_name)

#int, float, string, bool

age = 30 # int
score = 7.8 # float
active = True # bool: True | False (Mayuscula la primera letra)

print(age)
print(score)
print(active)

# Type: con type()podemos saber que tipo de valor es: int, float, string, bool, etc.

# declaramos en una variable el tipo de valor que es la variable first_name
result = type(first_name)
print(result)

# declaramos en la variable 'result_last_name' el tipo de valor de last_name
result_last_name = type(last_name)
print(result_last_name)

# declaramos en 'result_age' el tipo de variable de age
result_age = type(age)
print(result_age)

# declaramos en 'result_score' el tipo de valor de 'score'
result_score = type(score)
print(result_score)

# declaramos en 'result_active' el tipo de valor de 'active'
result_active = type(active)
print(result_active)

# en python no existen las constantes, pero podemos indicar a los dev que una variable es tipo constante mediante el uso de las mayusculas.

VERSION = 1.0
print(VERSION)

# Input: con input() podemos solicitar que el usuario ingrese algo desde el teclado

result = input('Ingresa tu nombre: ') # obtendremos los valores ingresados en tipo String
print('Se ingreso la palabra: ' + result)
print( type(result) )

# Vamos a pedirle al usuario que ingrese los valores solicitados con input()

input_name = input('Ingresa tu nombre: ')
input_age = input('Ingresa tu edad: ')
input_score = input('Ingresa tu calificacion: ')
input_active = input('El usuario se encuentra activo? si/no ')

print(input_name)
print(input_age)
print(input_score)
print(input_active)

# Cuando se imprime en pantalla con print, tambien podemos hacerlo de la siguiente forma
print(input_name, input_age, input_score, input_active)

# Tambien podemos saber el tipo de valor que tiene cada ingreso
print(type(input_name), type(input_age), type(input_score), type(input_active))

# los input() entrega un string, ahora vamos a convertir/castear a diferentes tipos de datos

input_name_string = str(input_name) # Originalmente es un string, pero podemos convertirlo con str
input_age_int = int(input_age) # lo convertimos a un entero
input_score_int = float(input_score) # lo convertimos a un numero flotante, punto decimal
input_active_bool = bool(input_active) # lo convertimos a un boleano (hacerlo asi esta incorrecto)

# Imprimimos todo en una sola linea
print(input_name_string, type(input_name_string), input_age_int, type(input_age_int), input_score_int, type(input_score_int), input_active_bool, type(input_active_bool))

# ahora vamos a imprimir lo mismo pero en cada linea
print('Impreso en cada linea')
print(input_name_string, ' - ', type(input_name_string))
print(input_age_int, ' - ', type(input_age_int))
print(input_score_int, ' - ', type(input_score_int))
print(input_active_bool, ' - ', type(input_active_bool), 'No tiene un correcto Bool')

# Para trabajar con operadores boleanos debmos aprovechar las condicionales
# Operadores relacionales ( ==, !=, >, >=, <, <= )

input_active_bool = input_active == 'si'

print(input_active_bool, ' - ', type(input_active_bool), ' tendremos un correcto Bool')

# el str nos permite convertir todo a un string, es decir:

input_entero_string = input('dame un numero: ')
input_entero_string = str(input_entero_string)
print(input_entero_string, ' - ', type(input_entero_string))

# Fin de la clase
