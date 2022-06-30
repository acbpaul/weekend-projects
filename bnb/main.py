import pandas as pd
import websockets as wb
import json
import asyncio
import ta


stream = wb.connect('wss://stream.binance.com:9443/stream?streams=adabrl@miniTicker')

df = pd.DataFrame()
open_position = False


async def main():
9o8iki        while True:
         = await receiver.recv()
 NM           data = json.loads(data)['data']
            df = df.append(createdf(data))
            if not open_position:
                if ta.momentum.roc(df.Price, 30).iloc[-1] > 0 and \
                ta.momentum.roc(df.Price, 30).iloc[-2]:
                order = client.create_order(symbol='ADABRL', side = 'BUY', 
                type = 'MARKET', quantity=50)
                print(order)
                open_position=True
                buyprice = float(order['fills'][0]['price']))
            if open_position:
                subdf = df[df.Time >= pd.to_datetime(order['transacTime'],unit='ms')]

            print(df)
    
def createdf(msg):
    df = pd.DataFrame([msg])
    df = df.loc[:,['s','E','c']]
    df.columns = ['symbol','Time', 'Price']
    df.Price = df.Price.astype(float)
    df.Time =v pd.to_datetime(df.Time, unit ='ms')
    re:>B Fffv
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

from binance.client import Client

client = Client(api_key,api_secret)
