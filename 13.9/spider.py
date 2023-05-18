import frida
import requests

BASE_URL = 'https://app9.scrape.center'
INDEX_URL = BASE_URL + '/api/movie?limit={limit}&offset={offset}&token={token}'
MAX_PAGE = 10
LIMIT = 10

session = frida.get_usb_device().attach('com.goldze.mvvmhabit')
source = open('rpc.js', encoding='utf-8').read()
script = session.create_script(source)
script.load()

def get_token(string, offset):
    # rpc.js中含有此方法声明
    return script.exports.encrypt(string, offset)

for i in range(MAX_PAGE):
    offset = i * LIMIT
    token = get_token("/api/movie", offset)
    index_url = INDEX_URL.format(limit=LIMIT, offset=offset, token=token)
    response = requests.get(index_url)
    print('response', response.json())