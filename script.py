import schedule
import time
import pandas as pd
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def update_excel():
    try:
        # Fetch data from the CoinGecko API
        data = cg.get_coins_markets(vs_currency='usd', per_page=50, order='market_cap_desc')
        df = pd.DataFrame(data)[['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]
        
        # Calculate statistics
        top_5 = df.sort_values(by='market_cap', ascending=False).head(5)
        avg_price = df['current_price'].mean()
        max_change = df['price_change_percentage_24h'].max()
        min_change = df['price_change_percentage_24h'].min()
        
        # print the statistics to the console
        print("Top 5 coins by market cap:")
        print(top_5)
        print(f"Average Price: {avg_price}")
        print(f"Max 24h Change: {max_change}")
        print(f"Min 24h Change: {min_change}")

        # Write the updated DataFrame to Excel
        df.to_excel('live_crypto_data.xlsx', index=False)
        print("Excel file updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Schedule the update every 5 minutes
schedule.every(5).minutes.do(update_excel)

# Initial run
update_excel()

while True:
    schedule.run_pending()
    time.sleep(1)
