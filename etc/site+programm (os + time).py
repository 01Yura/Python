import os
import time

site=input('Введите название сайта: ')

if 'https://www.' in site:
    os.system('start ' + site)   
elif 'www' in site:
    os.system('start ' + 'https://' + site)
elif 'https://' not in site or 'www.' not in site:
    os.system('start ' 'https://www.' + site)

time.sleep(5)
os.startfile('C:\Program Files\WireGuard\wireguard.exe')
