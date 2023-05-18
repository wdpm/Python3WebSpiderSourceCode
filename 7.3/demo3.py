import asyncio
from pyppeteer import launch


async def main():
    await launch(headless=False)
    await asyncio.sleep(100)


asyncio.run(main())
