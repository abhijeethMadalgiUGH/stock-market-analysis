import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import csv

def getStockPrice(symbol, timestamp):
    # Parse the timestamp string into a datetime object
    timestamp=str(timestamp)
    timestamp_dt = datetime.strptime(timestamp, '%a %b %d %H:%M:%S +0000 %Y')
    timestamp_unix = int(timestamp_dt.timestamp())
    timestamp_dt = datetime.fromtimestamp(timestamp_unix)
    timestampBeforeSentiment = timestamp_dt - timedelta(days=1)
    timestampAfterSentiment = timestamp_dt + timedelta(days=1)
    
    try:
        # Fetch historical data for the specified date range
        print(symbol)
        data = yf.download(symbol, start=timestampBeforeSentiment, end=timestampAfterSentiment)
        
        # Check if data is valid
        if data is not None and not data.empty:
            return data
        else:
            print(f"No data available for {symbol} on {timestamp_dt}.")
            return None
            
    except Exception as e:
        print(f"Failed to download data for {symbol}: {e}")
        return None

# Reading the input csv file
df = pd.read_csv('./../datasets/stockerbot-export.csv', on_bad_lines='skip')

# Adding columns for one day before and after prices
df['OneDayBeforePrice'] = None
df['OneDayAfterPrice'] = None


with open('./../datasets/output_stockerbot.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['text','timestamp','source','symbols','company_names','OneDayBeforePrice','OneDayAfterPrice'])
    for index, row in df.iterrows():
        try:
            symbol = row['symbols']
            timestamp = row['timestamp']
        # Getting the stock price
            stockPrices = getStockPrice(symbol, timestamp)
            if stockPrices is not None:
                if not stockPrices.empty:
                    dayBeforePrice = stockPrices.iloc[0]['Close']
                    dayAfterPrice = stockPrices.iloc[-1]['Close']
                    writer.writerow([row['text'], row['timestamp'], row['source'], row['symbols'], row['company_names'], dayBeforePrice, dayAfterPrice])
                
        except:
            continue
# Saving the updated DataFrame back to the CSV file
