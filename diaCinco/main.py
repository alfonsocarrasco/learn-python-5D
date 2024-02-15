# Funciones

# En el siguiente ejemplo observamos que los print se van a ejecutar cuando la condicion de ejecute
#if <conditions>:
#    print('Hola')
#    print('Mundo')

# Para crear una funcion la hacemos de ls siguiente forma
# def name_function():
#   pass

def print_numbers():
        for number in range(1, 11):
            print(number)

print_numbers() # aqui invocamos la funcion



# creando una funcion que suma dos 10 + 20
def suma():
    result = 10 +20
    print(result)

suma()



# Datos de entrada de una funcion = Argumentos -> Parametros
def suma_parametros(number1, number2):
    return number1 + number2

print(suma_parametros(10,20))
print(suma_parametros(20,30))


def restar_parametros(number1, number2):
    return number1 - number2


def multiplicar_parametros(number1, number2):
    return number1 * number2

print(restar_parametros(2,1))
print(multiplicar_parametros(1,5))

# Ahora pediremos ingresar 5 calificaciones
# Dividermos por funciones

scores = []
for option in range(0,5):
    score = int(input('Ingresa una calificacion: '))
    scores.append(score)

print(scores)

# vamos a obtener el promedio
# una forma es

suma = 0
for score in scores:
    suma += score

average = suma / 5
average_len = suma / len(scores)

print('total:', suma, 'promedio: ', average, 'usando Len: ', average_len)

match average:
    case 10:
        print('Muchas felicidades aprobaste la materia')
    case 9 | 8:
        print('Aprobasete la materia')
    case 7:
        print('Aprobaste la materia, pero necesitas practicar mas')
    case _:
        print('Lo sentimos, no aprobaste la materia')

# Ahora vamos a extraer y crear las funciones

def set_scores():
    scores = []

    for option in range(0,5):
        score = int(input('Ingresa una calificacion: '))
        scores.append(score)
    
    return scores


def average(numbers):
    return sum(numbers) / len(numbers)

def show_message(average):
    match average:
        case 10:
            return print('Muchas felicidades aprobaste la materia')
        case 9 | 8:
            print('Aprobasete la materia')
        case 7:
            print('Aprobaste la materia, pero necesitas practicar mas')
        case _:
            print('Lo sentimos, no aprobaste la materia')
scores = set_scores()
avg = average(scores)
show_message(avg)

# Ahora vamos a encadenar las funciones

show_message(average(set_scores()))
