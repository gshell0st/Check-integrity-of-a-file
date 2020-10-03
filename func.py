import subprocess

#START
from colorama import init, Fore 

def backup():

    file = input(Fore.LIGHTYELLOW_EX+'[?] Input the file with the path here to backup: ')
    abre = open(file, "r")
    backup = open('backup', "w")
    backup.writelines(abre)

def compara():

    file = input(Fore.LIGHTYELLOW_EX+'[?] Input the file with the path here to check: ') 
    a = open(file, "r")
    abrea = a.readline()

    b = open('backup', "r")
    backa = b.readline()

    if backa == abrea:
        print(Fore.LIGHTGREEN_EX+'[+] The file is integrated [+]')

    else:
        print(Fore.LIGHTRED_EX+'[-] The file has been modified [-]')

    
