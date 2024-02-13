# Ya nos encontramos en la recta final de nuestra semana, y lo que haremos ahora, cómo ya es costumbre, será añadir más funcionalidades a nuestro programa.

# Puntualmente 4 nuevas funcionalidades. Aquí van.

# 1.- Ahora todos los valores que representan a un usuario: Nombre, apellidos, número de teléfono y correo electrónico deberán almacenarse en un diccionario.

# 2.- Se añadirá la opción de poder listar el ID de todos los usuarios registrados hasta el momento.

# 3.- Se añadirá la opción de poder ver la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID y a partir de este conocer la información registrada.

# 4.- Se añadirá la opción de poder editar la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID y a partir de este el programa pedirá nuevamente los valores de un registro para actualizarlos.

# Estas 3 nuevas opciones deberán ser presentadas al usuario al comienzo del programa, esto con la finalidad que sea el usuario quien defina que quiere hacer justo ahora: añadir nuevos usuario, consultarlos o editarlos.

# De igual forma el programa tendrán una quinta opción que le permita la usuario finalizar el programa cuando él lo desee.

# Un Tip. Para estas nuevas opciones puedes presentarle a tu usuario un pequeño menú del cual pueda elegir. Por ejemplo opción A.-) registrar nuevos usuarios, opción B.-) listar usuarios, Opción C.-) Editar usuarios y así sucesivamente.

users = []
flag = True
id_user_init = 876
while(flag):
    id_user = int(len(users)) + id_user_init
    print('🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸 🔸')
    print('Welcome 🥞. Please select a option: A, B, C, or D')
    print(' A) Create 🍤')
    print(' B) Read 🍥')
    print(' C) Update 🥮')
    print(' D) Delete 🥟')
    option = str(input(''))

    # Create User 🍤
    if(option == 'A' or option == 'a'):
        name = str( input('Name: '))
        lastname = str( input('Lastname: ') )
        phone = int(input('Phone [10 dig]: '))
        email = str(input('Email: '))
        users.append({'id': id_user, 'name': name, 'lastname': lastname, 'phone': phone, 'email': email })
    
        new_flag = input('Return to the Menu? Y/N: ')

        if(new_flag == 'N' or new_flag == 'n'):
            flag = False
    
    # Read Users 🍥
    elif(option == 'B' or option == 'b'):
        print('╔═══ ID ══╦════ NAME ════╦═══ LASTNAME ═══╦════ PHONE ═══╦═══ EMAIL ════╗')
        
        for user in users:
            print('║  ',user['id'], ' ║  ', user['name'], ' ║  ', user['lastname'], ' ║  ', user['phone'], ' ║ ', user['email'], ' ║')
        
        print('╚═══════════════════════════════════════════════════════════════════════╝')
        print('Total: ', len(users), ' Users registred 🥡.')
    
    # Update User 🥮
    elif(option == 'C' or option == 'c'):
        print('AQUI VA LA OPCION C')

