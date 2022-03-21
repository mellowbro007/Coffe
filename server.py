import asyncio
import random

import websockets
import json
from icecream import ic

types = {
    'Cafe_Creme': 8,
    'Cappuccino': 10,
    'Easy_Clean': 3,
    'Espresso': 8,
    'Hot_Water': 2,
    'Latte_macchiato': 10,
    'Milchschaum': 2,
    'Warme_Milch': 2
}


async def send_coffee(websocket):
    while True:
        key = random.choice(list(types.keys()))
        data = json.dumps({
            'coffee_type': key,
            'position': random.randint(1, types[key])
        })
        ic(data)

        await websocket.send(data)
        await asyncio.sleep(3)

ic('starting server ..')
start_server = websockets.serve(send_coffee, '127.0.0.1', 7777)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
