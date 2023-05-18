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
}, verify=False)

response_index = requests.get(INDEX_URL, verify=False)
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)

# Response Status 200
# Response URL https://login2.scrape.center/login?next=/page/1
# 没有登录成功，session不一致，导致登录凭证丢失