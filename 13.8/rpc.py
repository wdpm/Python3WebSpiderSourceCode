import frida
import requests

BASE_URL = 'https://app8.scrape.center'
INDEX_URL = BASE_URL + '/api/movie?limit={limit}&offset={offset}&token={token}'
MAX_PAGE = 10
LIMIT = 10

session = frida.get_usb_device().attach('com.goldze.mvvmhabit')
source = open('rpc.js', encoding='utf-8').read()
script = session.create_script(source)
script.load()


def get_token(offset):
    return script.exports.encrypt("/api/movie", offset)


for i in range(MAX_PAGE):
    offset = i * LIMIT
    token = get_token(offset)
    index_url = INDEX_URL.format(limit=LIMIT, offset=offset, token=token)
    print(index_url)
    response = requests.get(index_url)
    print('response', response.json())
