from db_controller import connection, cursor
from db_model import Manager
import os

db_manager = Manager(cursor)
options=['1','2','3','4','5','6']
menu=[
    '[1] Insertar oficina',
    '[2] Insertar empleado',
    '[3] Mostrar todas las oficinas',
    '[4] Mostrar todos los empleados',
    '[5] Mostrar las oficinas de un empleado en especifico',
    '[6] Salir',
]
while True:
    #Prompt
    os.system('cls' if os.name == 'nt' else 'clear')
    print(*menu, sep='\n')
    option=input('> ')
    if option in options:
        #1
        if option == '1':
            #Renato
            pass
        #2
        if option == '2':
            name = input("Name: ")
            lastName = input("Last name: ")
            gender = input("Gender: ")
            birth_date = input("Birthdate YYYY-MM-DD: ")
            officeId = int(input("Office id: "))
            db_manager.insertEmployee(name,lastName,gender,birth_date,officeId)
            connection.commit()
            input()
        #3
        if option == '3':
            print(cursor.execute('SELECT * FROM office'))
        #4
        if option == '3':
            pass
        #5
        if option == '3':
            pass
        if option == '3':
            pass
    else:
        #Prompt for invalid input
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid option')
        input()
        continue
