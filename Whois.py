#!/usr/bin/python3


from socket import *
from colorama import Fore
import os
import sys

os.system('clear')
os.system('cls')
def banner():
    print(Fore.RED+"""


 .S     S.    .S    S.     sSSs_sSSs     .S    sSSs  
.SS     SS.  .SS    SS.   d%%SP~YS%%b   .SS   d%%SP  
S%S     S%S  S%S    S%S  d%S'     `S%b  S%S  d%S'    
S%S     S%S  S%S    S%S  S%S       S%S  S%S  S%|     
S%S     S%S  S%S SSSS%S  S&S       S&S  S&S  S&S     
S&S     S&S  S&S  SSS&S  S&S       S&S  S&S  Y&Ss    
S&S     S&S  S&S    S&S  S&S       S&S  S&S  `S&&S   
S&S     S&S  S&S    S&S  S&S       S&S  S&S    `S*S  
S*S     S*S  S*S    S*S  S*b       d*S  S*S     l*S  
S*S  .  S*S  S*S    S*S  S*S.     .S*S  S*S    .S*P  
S*S_sSs_S*S  S*S    S*S   SSSbs_sdSSS   S*S  sSS*S   
SSS~SSS~S*S  SSS    S*S    YSSP~YSSY    S*S  YSS'    
                    SP                  SP           
                    Y                   Y            
    """+Fore.BLUE+"         Author "":"+Fore.LIGHTYELLOW_EX+" Mrx_ali \n")

def whois():
    try:
        Domain = input(Fore.RED+" ┌─["+Fore.GREEN+"Enter The Domain --> "+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"☩ "+Fore.WHITE).lower()

        Domain = Domain.replace('http://', '')
        Domain = Domain.replace('https://' , '')
        Domain = Domain.replace('www.' , '')
        print(Fore.LIGHTYELLOW_EX+'\n ******************************************* ')
        print(Fore.LIGHTYELLOW_EX+'               please white ')
        if Domain[-3:] == 'org' or Domain[-3:] == 'net' or Domain[-3:] == 'com':
            whois_server = "whois.internic.net"

        else:
            whois_server = "whois.iana.org"    

        sock = socket(AF_INET , SOCK_STREAM)
        sock.connect((whois_server , 43))
        sock.send((Domain+'\r\n').encode())
        msg = sock.recv(10000)
        print(Fore.GREEN+msg.decode())
    except KeyboardInterrupt:
        print(Fore.RED+"\n Exit ")
    except:
        print(Fore.RED+"\n [!] please check Domian or internet ")

banner()
whois()

while True:
    try:
        print(Fore.LIGHTYELLOW_EX+'\n ************************************************************************************** ')
        print(Fore.LIGHTMAGENTA_EX+'\n\n [?] Do you want to continue? \n')
        user = input(Fore.RED+" ┌─["+Fore.GREEN+"Enter The Yes(Y) No(N) --> "+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"☩ "+Fore.WHITE).lower()
        if user.lower() == 'y' or user.upper() == 'Y':
            os.system('clear')
            os.system('cls')
            banner()
            whois()
        if user.lower == 'n' or user.upper() == 'N':
            print(Fore.RED+'\n Exit ')
            sys.exit()
        else:
            print('please Enter correctly ')
            
    except KeyboardInterrupt:
        print(Fore.RED+'\n Exit')
        sys.exit()

