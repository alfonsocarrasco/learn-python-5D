# Para este segundo reto de la seman tu objetivo será incrementar el funcionamiento del programa del día de ayer. Si recordamos, ayer construimos un programa en Python capaz de registrar un nuevo usuario en el sistema. Pues bien, continuando con el proyecto, el reto de hoy será que podremos registrar un N cantidad de nuevos usuarios.

# Para esto el programa deberá preguntar cuando nuevos usuarios se pretenden registrar.

# Si el por ejemplo coloco 5, bueno, serán 5 nuevos usuarios los que se deben capturar, usuarios con sus correspondientes valores: Nombre, apellidos, número de teléfono y correo electrónico.

# Además de todo esto, añadiremos una capa extra de seguridad, implementando un par de validaciones sobre los valores que se pueden ingresar.

# Validaremos que, tanto nombre, apellidos como correo electrónico tengan una longitud mínimo de 5 caracteres y un longitud máxima de 50.

# Así mismo el número de teléfono será a 10 dígitos.

# Si por alguna razón el usuario ingresa mal alguno de estos datos, el programa deberá notificarle y no permitirá continuar hasta que se ingresen datos correctos.

print('Bienvenido 🥞. Registrate con nosotros completando los siguientes datos:')
print('🔵 Nombre(s)')
print('🔵 Apellidos')
print('🔵 Teléfono')
print('🔵 Email')

cantidad_registros = 1

cantidad_total_registros = input('Cuantos usuarios quieres registrar? ')
cantidad_registros = int(cantidad_total_registros)
while cantidad_registros >= 1:
        
    nombres = input('Cual es tu nombre? ')
    nombres = str(nombres)
    if len(nombres) < 5 and len(nombres) > 50:
        print('No puedes ingresar un nombre menor a 5 caracteres o mayor a 50.')
    else:
        apellidos = input('Cuales son tus apellidos? ')
        apellidos = str(apellidos)
        if len(apellidos) < 5 and len(apellidos) > 50:
            print('El apellido no puede ser menor a 5 caracteres o mayor a 50')
        else:
            telefono = input('Cual es tu telefono (10 digitos)? ')
            telefono = str(telefono)
            if len(telefono) < 10:
                print('El telefono debe ser a 10 digitos')
            else:
                email = input('Cual es tu correo electrónico? ')
                email = str(email)
                if len(email) < 5 and len(email) > 50:
                    print('Error en el correo electronico')
                else:
                    print('🖐️ Hola ', nombres, ', en breve recibirás un correo a: ', email)
                    cantidad_registros -= 1
