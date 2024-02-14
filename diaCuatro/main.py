# Cuarta clase
# Trabajaremos con Tuplas y Diccionarios

# Tuplas - Diccionarios

# TUPLAS
# - Se rige por medio de un indice
# - Es inmutable a diferencia de una lista -NO PUEDEN MOFICARSE-

# para crear una Tupla se usan parentesis
settings = ('localhost', 3306,  'root', 'password', 'database')
print(settings)

print(type(settings))

# las tuplas tienen indices

print('total: ',len(settings))
print(settings[0], settings[3], settings[-1])

# aqui tendremos una tupla a partir de otra tupla desde el indice 2 hasta el ultimo
settings_two = settings[2:]
print(settings_two)

# Aqui generamos una tupla aparti de otra tupla de forma inversa con ::-1
settings_three = settings[::-1]
print(settings_three)

# Podemos desacoplar los vales de una cupla,
host = settings[0]
port = settings[1]
user = settings[2]
password = settings[3]
name_db = settings[4]

print(host, port, user, password, name_db)

# Pero podemos hacerlo mejor con es desempaquetado
host_two, port_two, user_two, password_two, name_db_two = settings
print('Ahora vamos a desempaquetar la data:')
print(host_two, port_two, user_two, password_two, name_db_two)

# Cuando desempaquetamos tambien podemos ignorar ciertas variables
print('Desempaquetamos ignorando las ultimas 3 variables')
host_three, port_three, _, _, _, = settings
print(host_three, port_three)

# Ahora si tenemos una tupla con muchos valores, no necesitamos poner _ para ignorar las variables
print('Desempaquetando la tupla')
host_four, port_four, *_= settings
print(host_four, port_four)

# Vamos ahora a crear una tupla de tuplas
tuples = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    )
print(tuples)

for _tuple in tuples:
    print(_tuple)

for _index, _tuple in enumerate(tuples):
    for _index_number, number in enumerate(_tuple):
        print(_index, number, _index_number)

# DICCIONARIOS
# Llave : Valor

user = {
        'name' : 'Alfonso',
        'email' : 'alfonso@gmail.com',
        'active' : True,
        10 : 3.14,
        True : 'Verdadero',
        (1, 2, 3) :'Tupla'
    }
print('Imprimimos el diccionario: ')
print(user);
print('Tambien lo podemos hacer accediendo a su llave')
print(type(user),user['name'], user['active'])
print('Extendiendo el diccionario, imprimiendo mas datos')
print(user[10])
print(user[True])
print(user[(1, 2, 3)])

# Usando metodo Get en los diccionarios
# debemos esperar que se genere un None (eso arroja el metodo get cuando no encuentra una llave)
value = user.get('username')
print(value)

# Metodos: Keys, Values, Items
# keys method
print('Obteniendo las keys del diccionario:')
print(user.keys())

# values method
print('Obteniendo los Values')
print(user.values())

# items method
print('Obteniendo los items')
print(user.items())

# desempaquetamos diccionario convirtiendo a una tupla

for clave, valor in tuple ( user.items() ):
    print(clave, valor)
