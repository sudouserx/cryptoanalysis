# Crypto Analysis

This repository contains a Python project that fetches live cryptocurrency data for the top 50 cryptocurrencies using the CoinGecko API, performs basic analysis, and updates a Google Sheet with the latest data every 5 minutes. This allows you to monitor market trends in near real time.

## Features

- **Live Data Fetching:** Retrieves live data for the top 50 cryptocurrencies by market capitalization.
- **Data Analysis:** Computes key metrics:
  - Top 5 cryptocurrencies by market cap.
  - Average price of the top 50 cryptocurrencies.
  - Highest and lowest 24-hour percentage price changes.
- **Google Sheets Integration:** Automatically updates a Google Sheet with the latest data every 5 minutes.
- **Real-Time Console Logging:** Prints analysis results to the console for monitoring and debugging.

## Prerequisites

- **Python 3.6+**
- A [Google Cloud Project](https://console.cloud.google.com/) with the following APIs enabled:
  - Google Sheets API
  - Google Drive API
- A service account with credentials (download the JSON key file) and permissions to edit your target Google Sheet.
- A Google Sheet created and shared with the service account's email.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/sudouserx/cryptoanalysis.git
   cd cryptoanalysis
   ```

2. **Install Required Python Packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Google API Credentials:**
   - Place your Google API credentials JSON file (e.g., `credentials.json`) in the project directory.
   - In the script (`script.py`), update the path to your credentials file:

     ```python
     gc = gspread.service_account(filename='path/to/credentials.json')
     ```

2. **Google Sheet Setup:**
   - Create or open your Google Sheet.
   - Share the Google Sheet with the service account email found in your credentials JSON file.
   - In `script.py`, update the `sheet_url` variable with your Google Sheet URL:

     ```python
     sheet_url = 'https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit?usp=sharing'
     ```

## Usage

Run the script using Python:

```bash
python script.py
```

When executed, the script will:

- Fetch live cryptocurrency data from the CoinGecko API.
- Perform analysis and display key metrics in the console.
- Update your specified Google Sheet with the latest data every 5 minutes.

## Analysis Report

A brief analysis report is generated through the console output, highlighting:
- The top 5 cryptocurrencies by market cap.
- The average price of the top 50 cryptocurrencies.
- The highest and lowest 24-hour percentage price changes.

You can capture this output for your records or expand the script to save these insights into a separate report file.

## Troubleshooting

- **Google Sheets Not Updating:**  
  Ensure your credentials are correct and that the Google Sheet is shared with your service account.
  
- **API/Data Errors:**  
  Verify your internet connection and check the CoinGecko API status if you encounter issues fetching data.

## Contributing

Contributions and enhancements are welcome! Please fork this repository and submit pull requests for improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [CoinGecko API](https://www.coingecko.com/en/api) for providing comprehensive cryptocurrency data.
- [gspread](https://github.com/burnash/gspread) and [gspread-dataframe](https://github.com/robin900/gspread-dataframe) for facilitating Google Sheets integration.
- [Schedule](https://schedule.readthedocs.io/) for enabling simple task scheduling in Python.
```