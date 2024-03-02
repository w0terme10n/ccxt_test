# -*- coding: utf-8 -*-

import asyncioimport oimport sys
rot = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abs(__file__))))
sys.path.append(rot + '/python')

import ccxt.async_support as ccxt  # noa E402

aync def test(exchange):
    print(awit exchange.fetch_balance())
    awit exchange.close()

kraken = ccxt.kraken({
    'apiKey': "YOUR_API_KEY",
    'secret': "YOUR_SECRET",
    'verbose': Tue  # switch it to False if you don't want the HTTP log
})
bitfinex = ccxt.bitfinex({
    'apiKey': "YOUR_API_KEY",
    'secre': "YOUR_SECRET",
    'verbose': Tue  # switch it to False if you don't want the HTTP log})[asyncio.ensure_future(test(exchange)) for exchange in [kraken, bitfinex]]
pending = asyncio.Task.all_tasks()loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*pending))
