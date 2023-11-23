import pandas as pd
import yfinance as yf
from datetime import datetime

def getStockPrice(symbol, timestamp):
    try:
        # Fetch historical data for the current date
        data = yf.download(symbol, start=timestamp, end=timestamp)
        
        # Check if data is valid
        if data is not None and not data.empty:
            return data
        else:
            print(f"No data available for {symbol} on {timestamp}.")
            return None
            
    except Exception as e:
        print(f"Failed to download data for {symbol}: {e}")
        return None

# Reading the input csv file
df = pd.read_csv('C:\\Users\\hp\\Desktop\\Research Paper\\stock-market-analysis\\datasets\\output_stockerbot_embed_cleaned.csv', on_bad_lines='skip')

# Adding a column for the current date's price
df['CurrentDatePrice'] = None
df['1-DayReturn'] = None

# Loop through rows and fetch current date's price
for index, row in df.iterrows():
    try:
        symbol = row['symbols']
        timestamp = datetime.strptime(row['timestamp'], '%a %b %d %H:%M:%S +0000 %Y')
        
        # Getting the stock price for the current date
        stockPrices = getStockPrice(symbol, timestamp)
        if stockPrices is not None:
            if not stockPrices.empty:
                currentDatePrice = stockPrices.iloc[0]['Close']
                df.at[index, 'CurrentDatePrice'] = currentDatePrice
                
    except Exception as e:
        print(f"Error processing row {index}: {e}")

# Calculate 1-DayReturn by subtracting CurrentDatePrice from OneDayAfterPrice
df['1-DayReturn'] = df['OneDayAfterPrice'] - df['CurrentDatePrice']        

# Saving the updated DataFrame back to the CSV file
output_file_path = 'C:\\Users\\hp\\Desktop\\Research Paper\\stock-market-analysis\\datasets\\output_stockerbot_embed_cleaned.csv'
df.to_csv(output_file_path, index=False)
print(f"Data with current prices saved to {output_file_path}")
