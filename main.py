# -*- coding: utf-8 -*-
import argparse
import json
import os
from datetime import datetime
import os.path
title = """\
 ███▄    █  ██▓  █████▒▄▄▄█████▓ ▒█████   ██▀███   ██▓ ▄▄▄      
 ██ ▀█   █ ▓██▒▓██   ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▓██▒▒████▄    
▓██  ▀█ ██▒▒██▒▒████ ░ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒▒██▒▒██  ▀█▄  
▓██▒  ▐▌██▒░██░░▓█▒  ░ ░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  ░██░░██▄▄▄▄██ 
▒██░   ▓██░░██░░▒█░      ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒░██░ ▓█   ▓██▒
░ ▒░   ▒ ▒ ░▓   ▒ ░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▓   ▒▒   ▓▒█░
░ ░░   ░ ▒░ ▒ ░ ░          ░      ░ ▒ ▒░   ░▒ ░ ▒░ ▒ ░  ▒   ▒▒ ░
   ░   ░ ░  ▒ ░ ░ ░      ░      ░ ░ ░ ▒    ░░   ░  ▒ ░  ░   ▒   
         ░  ░                       ░ ░     ░      ░        ░  ░                                                              
"""
# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("-H", "--host", required=True, type=str, help = "Attacking IP (ex: 10.10.10.10")
parser.add_argument("-P", "--port", required=True, type=int, help = "Attacking port (ex: 4444) ")
parser.add_argument("-OS", "--system", required=True, type=str, help = "Victim OS (ex: linux, windows, macos)")
parser.parse_args()
args = parser.parse_args()

if __name__ == "__main__":
    print(f"{title}\n\nIP: {args.host}\nPort: {args.port}\nOS: {args.system}\n")
    #Check revShellOutput dir
    dbLinux, dbMacOS, dbWindows = True, True, True
    if(os.path.isdir('revShellOutput')):
        print("\033[92mReverse shell Dir [\u2713] \033[0m")
    else: 
        os.makedirs('revShellOutput')
        print("\033[92mReverse shell Dir [Created] \033[0m")
    #Check dbLinux
    if(os.path.isfile('db/dbLinux.json')):
        print("\033[92mLinux Reverse Shell Database [\u2713] \033[0m")
    else: 
        print("\033[93mLinux Reverse Shell Database [\u2717] \033[0m")
        dbLinux = False
    #Check dbMacOS
    if(os.path.isfile('db/dbMacOS.json')):
        print("\033[92mMacOS Reverse Shell Database [\u2713] \033[0m")
    else: 
        print("\033[93mMacOS Reverse Shell Database [\u2717] \033[0m")
        dbMacOS = False
    #Check dbWindows
    if(os.path.isfile('db/dbWindows.json')):
        print("\033[92mWindows Reverse Shell Database [\u2713] \033[0m")
    else: 
        print("\033[93mWindows Reverse Shell Database [\u2717] \033[0m")
        dbWindows = False
    if(not dbLinux or not dbWindows or not dbMacOS):
        print("\n\033[91m\033[1mMissing database\033[0m")
        sys.exit()

    if(args.system):
        db = json.loads(json.dumps(json.load(open(f'db/db{args.system.lower().capitalize()}.json'))))
        print("\n[0] -> Exit")
        for revshell in db:
            print(f'''[{revshell["uniqueID"]}] -> {revshell["name"]} {"(File)" if(revshell["isFile"])else "(Bash)"}''')

        choice  = int(input("> "))
        if choice <= len(db):
            for revshell in db:
                if choice == revshell["uniqueID"]:
                    if(revshell["isFile"] == False):
                        print(f'\nReverse shell:\n{revshell["reverseShell"].replace("ATTACKER_IP", str(args.host)).replace("ATTACKER_PORT", str(args.port))}\nListener:\n{revshell["listener"].replace("ATTACKER_PORT", str(args.port))}\n')
                    else: 
                        rev = open(revshell['path'], "r")
                        today = datetime.today()
                        nameFiletmp = today.strftime("%d_%m_%Y_%H:%M:%S")
                        nameFile = input(f'Save file as: (default is {nameFiletmp}{revshell["extension"]}): ')
                        nameFile = nameFile if nameFile else nameFiletmp
                        path = f'revShellOutput/{nameFile}{revshell["extension"]}'
                        with open(path, 'w+') as file:
                            print(rev.read().replace("ATTACKER_IP", str(args.host)).replace("ATTACKER_PORT", str(args.port)), file=file)
                        if os.path.isfile(path):
                            print (f"\033[92m\033[1mFile created!\033[0m\nPath: {os.path.abspath(path)}")
                        else: print("Error while creating/writing file")
                        rev.close()
        else: print("Insert a valid number")


