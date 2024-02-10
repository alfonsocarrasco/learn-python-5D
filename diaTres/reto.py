# Vaya, ya llegamos al reto número 3 de la semana, y para este tercer reto lo que haremos será añadir 2 nuevas funcionalidades a nuestro programa de registro de usuarios.

# Estas funcionalidades son las siguientes

# 1.- Siempre que se registre un nuevo usuario de forma exitosa generaremos un identificador único para este registro/usuario. Te recomiendo sea un ID numérico auto incremental, que comience en 1 hasta N. Sin embargo siéntete libre elegir el formato o tipo que tú desees.
# 2.- Todos estos nuevos identificadores deberán almacenarse en un listado que será impreso en consola cuando todos los registros se hayan creado. Esto de tal forma que el usuario pueda conocer y tenga certeza que las operaciones, en efecto, se realizaron de forma exitosa.

# Con estas 2 nuevas funcionalidades es probable te intuyas como iremos finalizando nuestro programa para el quinto día.

print('Bienvenido 🥞. Registrate con nosotros completando los siguientes datos:')
print('🔵 Nombre(s)')
print('🔵 Apellidos')
print('🔵 Teléfono')
print('🔵 Email')

cantidad_total_registros = input('Cuantos usuarios quieres registrar? ')
cantidad_registros = int(cantidad_total_registros)
usuarios_registrados = []
id_usuario = 1357
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
                    print('Registro guardado !!!')
                    registro = 'Hola ' + nombres + ' en breve recibiras un correo a: ' + email;
                    usuarios_registrados.append([id_usuario, [nombres, apellidos, telefono, email], registro])
                    cantidad_registros -= 1
                    id_usuario +=1

if len(usuarios_registrados) == int(cantidad_total_registros):
    for usuario in usuarios_registrados:
        print(usuario)
