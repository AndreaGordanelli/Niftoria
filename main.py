# -*- coding: utf-8 -*-
#https://ozzmaker.com/add-colour-to-text-in-python/
#TODO: add colour
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
    if(args.system.lower() == "linux"):
        db = json.loads(json.dumps(json.load(open('db/dbLinux.json'))))
        for revshell in db:
            print(f'''[{revshell["uniqueID"]}] -> {revshell["name"]}''')

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
                            print (f"File created!\nPath: {os.path.abspath(path)}")
                        else: print("Error while creating/writing file")
        else: print("Insert a valid number")


