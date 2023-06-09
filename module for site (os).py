import os

site=input('Enter website: ')

if 'https://www.' in site:
    os.system('start ' + site)
    print('if')    
elif 'www' in site:
    os.system('start ' + 'https://' + site)
    print('elif')
elif 'https://' not in site or 'www.' not in site:
    os.system('start ' 'https://www.' + site)
    print('else')

##последний блок с ELIF можно заменить на более простой
##else:
##    os.system('start ' 'https://www.' + site)
##    print('else')
    
