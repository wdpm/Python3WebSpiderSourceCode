import requests
from urllib.parse import urljoin

BASE_URL = 'https://login2.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

response_login = requests.post(LOGIN_URL, data={
    'username': USERNAME,
    'password': PASSWORD
}, allow_redirects=False,verify=False)

cookies = response_login.cookies
print('Cookies', cookies)
# Cookies <RequestsCookieJar[<Cookie sessionid=j7pfx7dk62x1mg52huz30j25g8g3clrk for login2.scrape.center/>]>

response_index = requests.get(INDEX_URL, cookies=cookies,verify=False)
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)
print('Response URL', response_index.text.__contains__("/logout"))

# Response Status 200
# Response URL https://login2.scrape.center/page/1

# 这种方式比较麻烦，因为需要手动传递cookie
