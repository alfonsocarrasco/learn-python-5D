# Estructuras de control
# if, match ( en php, js es switch), foreach, while
# Bool - True | False
# debe ser con la T mayuscula para True 
# debe ser con la F mayuscula para False
result = False
print(result)

# Para usar Booleanos en Python podemos usarlos con:
# Operadores relaciones ( ==, !=. >, >=, <, <= )
# Operadores logicos (and, or, not)

number1 = 10
number2 = 20

# vamos a usar los operadores relaciones guardando en una variable el resultado

result = number1 == number2
print(result, ' ', number1, ' == ', number2, ' ', type(result))

result_dos = number1 != number2
print(result_dos, ' ', number1, ' != ', number2, ' ', type(result_dos))

result_tres = number1 > number2
print(result_tres, ' ', number1, ' > ', number2, ' ', type(result_tres))

result_cuatro = number1 >= number2
print(result_cuatro, ' ', number1, ' >= ', number2, ' ', type(result_cuatro))

result_cinco = number1 < number2
print(result_cinco, ' ', number1, ' < ', number2, ' ', type(result_cinco))

result_seis = number1 <= number2
print(result_seis, ' ', number1, ' <= ', number2, ' ', type(result_seis))

# Nos damos cuenta que los operadores relaciones siempre nos daran un resultado boolean

# Vamos a usar operaciones logicos combinando con los Operadores logicos

print('Usando los operadores logicos')

result_logico_uno = number1 < number2 and 10 == 10
print(result_logico_uno, ' ', number1, ' < ', number2, ' and 10 == 10', type(result_logico_uno))

result_logico_dos = number1 < number2 and 10 == 10 and 5 != 5
print(result_logico_dos, ' ',number1, ' < ', number2, ' and 10 == 10 and 5 != 5', type(result_logico_dos))
