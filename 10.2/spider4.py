from urllib.parse import urljoin
from selenium import webdriver
import requests
import time

from selenium.webdriver.common.by import By

BASE_URL = 'https://login2.scrape.center'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

browser = webdriver.Chrome()
browser.get(BASE_URL)
browser.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(USERNAME)
browser.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(PASSWORD)
browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
time.sleep(10)

# get cookies from selenium
cookies = browser.get_cookies()
print('Cookies', cookies)
browser.close()

# set cookies to requests
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])

response_index = session.get(INDEX_URL, verify=False)
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)
