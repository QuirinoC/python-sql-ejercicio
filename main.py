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
    os.system('cls' if os.name == 'nt' else 'clear')
    print(*menu, sep='\n')
    option=input('> ')
    if option in options:
        pass
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid option')
        input()
        continue
