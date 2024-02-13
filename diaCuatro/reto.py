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
    if(option.lower() == 'a'):
        name = str( input('Name: '))
        lastname = str( input('Lastname: ') )
        phone = int(input('Phone [10 dig]: '))
        email = str(input('Email: '))
        users.append({'id': id_user, 'name': name, 'lastname': lastname, 'phone': phone, 'email': email })
    
        new_flag = input('Return to the Menu? Y/N: ')

        if(new_flag.lower == 'n'):
            flag = False
    
    # Read Users 🍥
    elif(option.lower() == 'b'):
        print('            🔹🔹🔹🔹🔹🔹🔹🔹 LIST USERS 🔹🔹🔹🔹🔹🔹🔹🔹🔹 ')
        print('╔═══ ID ══╦════ NAME ════╦═══ LASTNAME ═══╦════ PHONE ═══╦═══ EMAIL ════╗')
        
        if(len(users) == 0):
            print('║                              Users not found                          ║')
        for user in users:
            print('║  ',user['id'], ' ║  ', user['name'], ' ║  ', user['lastname'], ' ║  ', user['phone'], ' ║ ', user['email'], ' ║')
        
        print('╚═══════════════════════════════════════════════════════════════════════╝')
        print('Total: ', len(users), ' Users registred 🥡.')
        new_flag_read = input('Return to the Menu? Y/N: ')
        if(new_flag_read.lower() == 'n'):
            flag = False

    # Update User 🥮
    elif(option.lower() == 'c'): 
        
        if(len(users) >= 1):
            for user in users:
                print('╔═══ ID ══╦════ NAME ════╦═══ LASTNAME ═══╦════ PHONE ═══╦═══ EMAIL ════╗')
                print('║  ',user['id'], ' ║  ', user['name'], ' ║  ', user['lastname'], ' ║  ', user['phone'], ' ║ ', user['email'], ' ║')
        
                print('╚═══════════════════════════════════════════════════════════════════════╝')
            id_user_update = int(input('Enter ID User to update: '))
            flag_search = False
            for user in users:
                if(user['id'] == id_user_update):
                    flag_search = True
                    
                    print('Actual name: 👉' + user['name'] + '👈 Enter new Name: ')
                    new_name = input()
                    print('Actual lastname: 👉' + user['lastname'] + '👈 Enter new Lastname:')
                    new_lastname = input('')
                    print('Actual phone: 👉', user['phone'], '👈 Enter new Phone: ')
                    new_phone = int(input())
                    print('Actual email: 👉' + user['email'] + '👈 Enter new Email: ')
                    new_email = input()
                    user['name'] = new_name
                    user['lastname'] = new_lastname
                    user['phone'] = new_phone
                    user['email'] = new_email
                    
                    print('🍾 Update success 🍾')
                    print('╔═══ ID ══╦════ NAME ════╦═══ LASTNAME ═══╦════ PHONE ═══╦═══ EMAIL ════╗')
                    print('║  ',user['id'], ' ║  ', user['name'], ' ║  ', user['lastname'], ' ║  ', user['phone'], ' ║ ', user['email'], ' ║')
        
                    print('╚═══════════════════════════════════════════════════════════════════════╝')
            if(flag_search == False):
                print("Sorry, don't found user id: ", id_user_update)
            
        else:
            print('🔴 🔴 Not found Users to update 🔴 🔴')
        
        new_flag_update  = input('Return to the Menu? Y/N: ')
        if(new_flag_update.lower() == 'n'):
            flag = False
    # Delete User
    elif(option.lower() == 'd'):
        print('List Users')
        for user in users:
            print('╔═══ ID ══╦════ NAME ════╦═══ LASTNAME ═══╦════ PHONE ═══╦═══ EMAIL ════╗')
            print('║  ',user['id'], ' ║  ', user['name'], ' ║  ', user['lastname'], ' ║  ', user['phone'], ' ║ ', user['email'], ' ║')
            print('╚═══════════════════════════════════════════════════════════════════════╝')
            id_user_delete = int(input('Enter ID User to delete: '))
            for user in users:
                if(user['id'] == id_user_delete):
                    users.remove(user)

            print('Congratulations, Remove user 🍨')

            new_flag_delete = input('Return to the Menu? Y/N: ')
            if(new_flag_delete.lower() == 'n'):
                flag = false
