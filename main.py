# -*- coding: utf-8 -*-
import argparse
import json

'''
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
'''
title = "Niftoria"
# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("-H", "--host", required=True, type=str, help = "Attacking IP")
parser.add_argument("-P", "--port", required=True, type=int, help = "Attacking port")
parser.add_argument("-OS", "--system", required=True, type=str, help = "Victim OS (linux, windows, macos)")
parser.parse_args()
args = parser.parse_args()


if __name__ == "__main__":
    print(f"{title} Attacking on {args.system}")
    args = parser.parse_args()
    
    if(args.system.lower() == "linux"):
        db = json.loads(json.dumps(json.load(open('dbLinux.json'))))
        for revshell in db:
            print(f'''{revshell["uniqueID"]} > {revshell["name"]}''')

