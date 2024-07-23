import colorama
import mcuuid
import random
import os
from colorama import *
from tkinter import *
import soundfile as sf
import soundcard as sc
from alive_progress import alive_bar
from email import *
import subprocess
import platform
import sys
import time

colorama.init(autoreset=True)

tjtas1 = '''
    ╔══╦═╦══╦═╦═╗
    ╚╗╔╩╗╠╗╔╣═║╚╣
     ║║╔║║║║║║╠╗║
     ╚╝╚═╝╚╝╚╩╩═╝
'''

def clean():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clean()

with alive_bar(100) as bar:
        for i in range(100):
            time.sleep(0.06)
            bar()

print(Fore.RED + "loading successful")
clean()

print(tjtas1)

run = True

while run:
    help1 = Fore.RED + '''commands:
        uuid
        quit
        discord
        ripg
        james
        cls'''
    print(Fore.BLUE + "    windows@Tjtas ~")
    inp = str(input(Fore.RED + "    ↪ " + Fore.RESET))
    if inp == "help":
        print(help1)
    elif inp == "uuid":
        uuid = mcuuid.MCUUID(name=input(Fore.BLUE + "insert the player's name: " + Fore.RESET))
        print(uuid.uuid)
    elif inp == "quit":
        run = False
    elif inp == "discord":
        print("https://discord.gg/tg744FvmfM")
    elif inp == "ripg":
        po = random.randrange(1, 999)
        pi = random.randrange(1, 999)
        pu = random.randrange(1, 999)
        ae = random.randrange(1, 999)
        print(str(po) + "." + str(pi) + "." + str(pu) + "." + str(ae))
    elif inp == "cls":
        clean()
        print(tjtas1)
    elif inp == "nycd":
        clean()
        print(f"□ □ {Fore.RED}■ ■ ■ ■ ■ ■ ■ {Fore.RESET}□ □ □")
        print(f"□ {Fore.RED}■ ■ ■ ■ ■ ■ ■ ■ ■ {Fore.RESET}□ □")
        print(f"{Fore.RED}■ ■ {Fore.RESET}□ □ □ □ □ □ □ {Fore.RED}■ {Fore.RESET}□ □")
        print(f"{Fore.RED}■ {Fore.RESET}□ □ □ □ □ □ □ □ {Fore.RED}■ {Fore.RESET}□ □")
        print(f"{Fore.RED}■ {Fore.RESET}□ □ □ □ □ □ □ □ {Fore.RED}■ ■ ■")
        print(f"{Fore.RED}■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
        print(f"□ {Fore.RED}■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
        print(f"□ {Fore.RED}■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
        print(f"□ {Fore.RED}■ ■ ■ ■ {Fore.RESET}□ □ {Fore.RED}■ ■ ■ ■ ■")
        print(f"□ {Fore.RED}■ ■ ■ {Fore.RESET}□ □ □ □ {Fore.RED}■ ■ {Fore.RESET}□ □")
        print(f"□ {Fore.RED}■ ■ ■ {Fore.RESET}□ □ □ □ {Fore.RED}■ ■ {Fore.RESET}□ □")
        run = False
    else:
        print(Fore.RED + "Unknown command")