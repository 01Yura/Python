import os
import time

while True:

    site=input('Введите название сайта: ')
    if site=='END':
        break

    if 'https://www.' in site:
        os.system('start ' + site)   
    elif 'www' in site:
        os.system('start ' + 'https://' + site)
    elif 'https://' not in site and 'www.' not in site and '.com' not in site:
        os.system('start ' 'https://www.' + site + '.com')
    elif 'https://' not in site or 'www.' not in site:
        os.system('start ' 'https://www.' + site)
