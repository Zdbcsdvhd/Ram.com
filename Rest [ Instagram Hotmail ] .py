import requests
from cfonts import render, say
try:
    pass
except:
    os.system('pip install python-cfonts')

THOMAS = render('{ RESET - HOTMAİL}', colors=['white', 'blue'], align='center')
print(f'''\n
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
     
                      {THOMAS}
    ~ Programmer : @GrayHacker_bot | Channel: @Hackeralokrenew ~
 
   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    
''')
email = input(" ~ Email Giriniz : ")
print("\x1b[1;39m—" * 60)
url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"

headers = {
    "authority": "www.instagram.com",
    "method": "POST",
    "path": "/api/v1/web/accounts/account_recovery_send_ajax/",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "csrftoken=BbJnjd.Jnw20VyXU0qSsHLV; mid=ZpZMygABAAH0176Z6fWvYiNly3y2; ig_did=BBBA0292-07BC-49C8-ACF4-AE242AE19E97; datr=ykyWZhA9CacxerPITDOHV5AE; ig_nrcb=1; dpr=2.75; wd=393x466",
    "origin": "https://www.instagram.com",
    "referer": "https://www.instagram.com/accounts/password/reset/?source=fxcal",
    "sec-ch-ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; M2101K786) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
    "x-asbd-id": "129477",
    "x-csrftoken": "BbJnjd.Jnw20VyXU0qSsHLV",
    "x-ig-app-id": "1217981644879628",
    "x-ig-www-claim": "0",
    "x-instagram-ajax": "1015181662",
    "x-requested-with": "XMLHttpRequest"
}

data = {
    "email_or_username": email,
    "flow": "fxcal"
}


response = requests.post(url, headers=headers, data=data)
H = '\x1b[1;32m'
#print(response.status_code)
print('\x1b[1;32m')
print(response.json())

# @t5omas