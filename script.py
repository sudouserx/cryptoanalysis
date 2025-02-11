import schedule
import time
import pandas as pd
from pycoingecko import CoinGeckoAPI
import gspread
from gspread_dataframe import set_with_dataframe

# Initialize the CoinGecko API client
cg = CoinGeckoAPI()

# Set up the Google Sheets client using service account credentials
gc = gspread.service_account(filename='cred.json')

# Open the Google Sheet by URL
sheet_url = 'https://docs.google.com/spreadsheets/d/1DnKU8Voi5C--d9QcJZjLZ3ZHdV2Tx_YVTUCo9p20S7g/edit?usp=sharing'
sh = gc.open_by_url(sheet_url)
worksheet = sh.sheet1 

def update_google_sheet():
    try:
        # Fetch data from the CoinGecko API for the top 50 cryptocurrencies by market cap
        data = cg.get_coins_markets(vs_currency='usd', per_page=50, order='market_cap_desc')
        
        # Create a DataFrame with the required fields
        df = pd.DataFrame(data)[['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]
        
        # Perform analysis
        top_5 = df.sort_values(by='market_cap', ascending=False).head(5)
        avg_price = df['current_price'].mean()
        max_change = df['price_change_percentage_24h'].max()
        min_change = df['price_change_percentage_24h'].min()
        
        # Print the statistics to the console (for debugging/monitoring)
        print("-------------------------------------------------")
        print("Live Cryptocurrency Data Analysis:")
        print("\nTop 5 Cryptocurrencies by Market Cap:")
        print(top_5.to_string(index=False))
        print(f"\nAverage Price: ${avg_price:.2f}")
        print(f"Highest 24h Change: {max_change:.2f}%")
        print(f"Lowest 24h Change: {min_change:.2f}%")
        print("-------------------------------------------------")
        
        # Update the Google Sheet with the new DataFrame
        set_with_dataframe(worksheet, df)
        print("Google Sheet updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Schedule the update every 5 minutes
schedule.every(5).minutes.do(update_google_sheet)

# Run the update once immediately to generate initial data
update_google_sheet()

# Continuously run the scheduler to update the Google Sheet live
while True:
    schedule.run_pending()
    time.sleep(1)
