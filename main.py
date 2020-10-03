from func import *
from colorama import init, Fore 

print(Fore.LIGHTGREEN_EX+'''
[!] Checkpoint of backup and check files [!]
       |
       |-> [1] Backup selection;
       |
       |-> [2] Check selection;
       |
       |-> [3] Exit;
''')

while True:
    escolha = int(input(Fore.LIGHTBLUE_EX+'[?] Choose the file for backup and check with or exit: '))

    if escolha == 1:
        backup()

    elif escolha == 2:
        compara()

    elif escolha == 3:
        exit()
