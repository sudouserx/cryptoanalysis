import schedule
import time
import pandas as pd
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
data = cg.get_coins_markets(vs_currency='usd', per_page=50, order='market_cap_desc')
df = pd.DataFrame(data)[['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]

top_5 = df.sort_values(by='market_cap', ascending=False).head(5)
avg_price = df['current_price'].mean()
max_change = df['price_change_percentage_24h'].max()
min_change = df['price_change_percentage_24h'].min()

print(avg_price)
def update_excel():
    df.to_excel('live_crypto_data.xlsx', index=False)

schedule.every(5).minutes.do(update_excel)
while True:
    schedule.run_pending()
    time.sleep(1)