from concurrent.futures import process
import os
from termcolor import colored
from pystyle import Write
import random
import time
import colorama
from os import system, name
from time import sleep
from pystyle import Write, Colors, Colorate, Box
from colorama import Fore, Back, Style

colorama.init()
import time
import random

def clear_console():
    if os.name == 'nt':  
        os.system('cls')
    else:
        print('\n' * 100)

clear_console()

def loading_screen():
    loading_message = "Loading... "
    animation_chars = ["|", "/", "-", "\\"]
    duration = 5
    start_time = time.time()
    
    while time.time() - start_time < duration:
        for char in animation_chars:
            print(f"\r{loading_message} {char}", end="")
            time.sleep(0.1)

    print("\r" + " " * len(loading_message), end="")

if __name__ == "__main__":
    loading_screen()
    print("\nLoading completed! ")
    
clear_console()

Write.Print(f'''
  ██╗███████╗ ██████╗ ██╗      █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
  ██║██╔════╝██╔═══██╗██║     ██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
  ██║███████╗██║   ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║
  ██║╚════██║██║   ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
  ██║███████║╚██████╔╝███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
  ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
        
     ╔══════════════════════════════════════════════════════════════╗
     ║ [1] Nitro Gen + Checker                    [10]        ║  
     ║ [2] Webhook Spammer                 [11]             ║
     ║ [3] CC Generator                [12]        ║
     ║ [4] Netflix Generator                [13]           ║
     ║ [5] Xbox GT Generator                       [14]         ║
     ║ [6] Hacking                                                ║
     ║ [7] Doxxing                [15] CREDITS               ║
     ║ [8] Token Checker             [17] EXIT                 ║
     ║ [9] Token Grabber                                            ║
     ╚══════════════════════════════════════════════════════════════╝
''', Colors.blue_to_cyan, interval=0.005)

print(Fore.LIGHTBLUE_EX)
choice = int(input("Choice:  "))

if choice == 1:
  import os
  import ctypes
  import requests
  import random
  import string
  import time
  print("")
  
  clear_console()

  num = int(input('How much codes to generate and check?: '))

  with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated!")

    start = time.time()

    for i in range(num):
      code = "".join(
        random.choices(string.ascii_uppercase + string.digits +
                       string.ascii_lowercase,
                       k=19))

      file.write(f"https://discord.gift/{code}\n")

  with open("Nitro Codes.txt") as file:
    for line in file.readlines():
      nitro = line.strip("\n")

      url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

      r = requests.get(url)

      if r.status_code == 200:
        print( f" Valid | {nitro} ")
        break
      else:
        print( f" Invalid | {nitro} ")

  time.sleep(0.2)

  print(
    "Valid codes will be in Valid Codes.txt - if there none then keep generating :)"
  )

elif choice == 2:
   import requests
   from discord_webhooks import DiscordWebhooks
   
   clear_console()

   webhook_url = input('Webhook URL: ')

   message = input('Enter Message: ')
   ilosc = int(input('Enter Amount of Messages: '))


   webhook = DiscordWebhooks(webhook_url)

   webhook.set_content(title='get spammed nigga ass cock',
                    description=message,
                    color=0xF58CBA)

   webhook.set_footer(text='made by scaigs')



   for i in range(ilosc):
       webhook.send()
elif choice == 9:
  pass # insert grebr koud here