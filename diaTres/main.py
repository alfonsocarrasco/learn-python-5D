# Tercera clase
# Trabajaremos listas en python
# Listas = EStructura de datos

my_list = [1, 3.14, 'String', True, [2, 3.111, "Example", False] ]
print(my_list, type(my_list))

my_list_two = [type(1), type(3.14)]
print(my_list_two)

# Lo mas recomendable es tener listas con el misto tipo de datos

courses = ['Python', 'Django', 'Flask', 'Ruby', 'Ruby on Rails', 'Rust', 'C#']
numbers = [1, 2, 3, 4]

print(courses)
print(numbers)

# Las listas se puede acceder por indices 0, 1, 2, 3, 4, 5, 6, etc... 
# Ademas las listas se puede acceder por -1, -2, -3, -4, -5, -6, etc...

print( courses[0], courses[1], courses[2] )

courses_total = len(courses)
last_index = courses_total - 1
print(courses_total, courses[last_index], last_index)

index = int(input('Ingresa el indice del cual quieres conocer su valor: '))

if index <= last_index:
    print(courses[index])
else:
    print('Lo sentimos, el indice no es valido')

# Vamos a crear una lista a partir de otra lista
# para ello solo necesitamos ingresar el inicio (indice) y el final (indice)
new_list = courses[0 : 1]
print(new_list)

# Tambien podemos agregar solo el inicio (indice) y despues vacio y con esto solito recorre hasta el final del indice
new_list_two = courses[3:]
print(new_list_two)

# Funciona para la inversa
new_list_three = courses[:5]
print(new_list_three)

# Tambien podemos copiar toda la lista usando
new_list_four = courses[:]
print(new_list_four)

# tambien podemos hacer saltos en la clonacion de la lista
new_list_five = courses[::2]
print(new_list_five)

# Tambien podemos clonar la lista y agregarlo de forma inversa, es decir
new_list_six = courses[::-1]
print(new_list_six)

# Metodos en list
# append, insert, extend, remove, clear, count, index. No son los unicos, existen muchos mas

# append se pueden agregar mas valores a las listas.
courses.append('Javascript')
courses.append('Typescript')
courses.append('Swift')

print(courses)

# insert, funciona para colocarlo en algun lugar del indice, desplazandolo
courses.insert(1, 'SqlServer')
print(courses)
print ('Cantidad de cursos: ', len(courses))

# ahora vamos agregar por medio del uso del metodo extend
new_courses = ['Java9', 'Docker', 'Unix']
courses.extend(new_courses)
print(courses)

print('Cantidad de cursos: ',len(courses))

# Ahora vamos a eliminar elementos de lista, para eso usamos remove

# Remove

print('Mostramos todo, incluye Typescript que luego vamos a eliminar')
print(courses)
courses.remove('Typescript')
print('vamos a eliminar Typescript')
print(courses)
# Ahora eliminamos otros elementos
courses.remove('Flask')
courses.remove('C#')
print('Eliminamos Flask y C#')
print(courses)

# Tambien podemos contar los elementos, para eso usamos el metodo count

# Count

# Aqui vamos a buscar la cantidad de veces que aparece el courso Ruby
print(courses.count('Ruby'))

# Podemos tambien saber por medio de un boleano si se encuentra Ruby en la lista

print('Buscamos si existe Ruby en courses: ','Ruby' in courses)

# Aqui vamos a generar intencionalmente un False, buscare Rubby
print('Buscamos si existe Rubby en courses: ', 'Rubby' in courses)

# Ahora vamos a buscar el indice en las listas con el metodo index

# Index

index_ruby = courses.index('Ruby')
print('Ruby tiene el index: ', index_ruby)

# vamos a agregar una sentencia if para buscar un indice

print('Ahora buscaremos un valor en la lista')
value = 'Java9'
if value in courses:
    print(' el valor: ', value, ' tiene el indice: ', courses.index(value))
else:
    print('parace que: ', value, ' no existe en la lista de cursos')

# ahora vamos a limpiar toda la lista con el metodo Clear

# Clear

print('La lista de cursos es: ',courses)
courses.clear()
print(' ahora la lista es: ', courses)

# Ahora vamos a iterar la lista de cursos usando for

# For

print('La lista que usaremos es: new_courses', new_courses)
for course in new_courses:
    print(course)

# Ahora vamos a agregar el indice de la lista
print('Conociendo los indices de las listas')
for index,course in enumerate(new_courses):
    print(course,index)

# Vamos a trabajar con un String iterable
text = 'Hola mundo'
print(text)

for character in text:
    print(character)

# ahora agregamos el indice del string que estamos iterando
for index, character in enumerate(text):
    print(character, index)

print ('Total caracteres ', len(text))

# Tambien podemos accesar a a los indices del texto de esta forma
print(text[0], 'indice 0')
print(text[5], 'indice 5')
print(text[0:4], 'Aqui estamos imprimiendo del indice 0 al 4')

# Parece que los string son inmutables, veamos si es cierto:
text[0] = 'P'
print(text)
