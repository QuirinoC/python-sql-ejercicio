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
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    #Prompt
    clear()
    print(*menu, sep='\n')
    option=input('> ')
    if option in options:
        clear()
        #1
        if option == '1':
            name = input("Name: ")
            db_manager.insertOffice(name)
            connection.commit()
        #2
        if option == '2':
            name = input("Name: ")
            lastName = input("Last name: ")
            gender = input("Gender: ")
            birth_date = input("Birthdate YYYY-MM-DD: ")
            officeId = int(input("Office id: "))
            db_manager.insertEmployee(name,lastName,gender,birth_date,officeId)
            connection.commit()

        #3
        if option == '3':
            print("Offices available")
            print(*cursor.execute('SELECT * FROM office').fetchall(),sep='\n')

        #4
        if option == '4':
            print("Employees available")
            print(*cursor.execute('SELECT * FROM employee').fetchall(),sep='\n')
        #5
        if option == '5':
            #Prompt the users in the database
            print(*cursor.execute('SELECT * FROM employee').fetchall(),sep='\n')
            id_ = input("Employee id > ")

            print(*cursor.execute(f'select * from office where id =(select officeId from employee where id={id_})').fetchall(),sep='\n')
        if option == '6':
            print("Bye bye")
            break;
        input()
    else:
        #Prompt for invalid input
        clear()
        print('Invalid option')
        input()
        continue
