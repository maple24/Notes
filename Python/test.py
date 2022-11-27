import asyncio
from time import sleep

async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print("done fetching")
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    asyncio.create_task(fetch_data())
    asyncio.create_task(print_numbers())
    
asyncio.run(main())


