import asyncio
import requests
import time

start = time.time()


async def get(url):
    return requests.get(url,verify=False)


async def request():
    url = 'https://httpbin.org/delay/2/'
    print('Waiting for', url)
    response = await get(url)
    print('Get response from', url, 'response', response)


tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)
