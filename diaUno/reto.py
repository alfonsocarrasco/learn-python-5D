# Para este primer reto de la semana, tu objetivo será poder crear un programa en Python el cual permita registrar a un usuario en el sistema.

# Para ello el programa deberá pedir a nuestro usuario final ingrese su siguiente información.

# Nombre(s).
# Apellidos.
# Número de teléfono.
# Correo electrónico.

# Una vez el usuario haya ingresado todos los datos vía teclado, el programa le dará la bienvenida al usuario con el siguiente mensaje:

# Hola + seguido del nombre completo del usuario +, en breve recibirás un correo a + seguido del correo electrónico.

print('Bienvenido 🥞. Registrate con nosotros completando los siguientes datos:')
print('🔵 Nombre(s)')
print('🔵 Apellidos')
print('🔵 Teléfono')
print('🔵 Email')

nombres = input('Cual es tu nombre? ')
nombres = str(nombres)

apellidos = input('Cuales son tus apellidos? ')
apellidos = str(apellidos)

telefono = input('Cual es tu telefono (10 digitos)? ')
telefono = int(telefono)

email = input('Cual es tu correo electrónico? ')
email = str(email)

print('🖐️ Hola ', nombres, ', en breve recibirás un correo a: ', email)

