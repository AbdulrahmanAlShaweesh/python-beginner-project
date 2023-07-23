
import cryptography.fernet as Fernet

# add user password


def add():
    name = input('enter your name ? ').strip().lower()
    password = input('enter your password ? ').strip()
    masterPassword = input('enter your master password ? ').strip()

    # with open will close the file automaticlly after we finish.
    with open('password_manager/password.txt', mode='a') as file:
        file.write(name + ' | ' + password + ' | ' + masterPassword + '\n')


def update():
    pass


def delte():
    pass

# view user passwords.


def view():
    name = input('enter your name ? ').strip().lower()
    user_data = {}

    with open('password_manager/password.txt', mode='r') as file:
        counter = 0
        for f in file:
            if counter == 0:
                pass
            else:
                data = f.split(' | ')
                user_data.update(
                    {data[0]: {'Password': data[1], 'MasterPassword': data[2].replace('\n', '')}})  # , 'Password': data[1], 'MasterPassword': data[2].replace('\n', '')
            counter += 1

    while name not in user_data.keys():
        error_mesg = input(
            'You name is not exits, would you like to view user password with your master password? ').strip()

        if error_mesg != 'yes':
            continue
        else:
            masterPassword = input(
                'enter your master password ? ').strip().lower()

            for i in user_data.values():
                if masterPassword in i.values():
                    for key, val in i.items():
                        print(key, val)
                    break
                else:
                    print(
                        'your master password is not valid,, please enter a valid master password')
                    continue
    else:
        # name, password, masterpassword = user_data[name].split(' | ')
        print(f'Name : {name}')
        print('Password : ' + user_data[name]['Password'])
        print('Master Password : ' + user_data[name]['MasterPassword'])


def passwordManager():
    while True:
        mode = input(
            'Would you like to add a new password, update the old password, delte the existing password or view the existing password (add/update/delete/view/q to exit)? ').strip().lower()

        if mode == 'q':
            print('you choose to exit the program')
            print('goodbye')
            break
        elif mode == 'add':

            add()
        elif mode == 'update':
            pass
        elif mode == 'delte':
            pass
        elif mode == 'view':
            view()
        else:
            print('you enter invalid option, please enter a valid option later.')
            continue


passwordManager()
