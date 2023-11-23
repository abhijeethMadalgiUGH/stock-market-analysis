import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import os

def download_save_stock_data(stock_symbol, output_filename):
    # Download historical stock data using yfinance
     if os.path.exists(output_filename):
        print(f"Data for {stock_symbol} already exists. Skipping download.")
        return
     else :
         end_date = str(datetime.today().date())
         start_date = str((datetime.today() - timedelta(days=365*10)).date())
         stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

         # Save the data to a CSV file
         stock_data.to_csv(output_filename)

if __name__ == "__main__":
    # Replace 'your_input_file.csv' with the actual path to your CSV file
    input_file_path = 'output_stockerbot_embed_cleaned.csv'

    # Read the CSV file using pandas
    stock_df = pd.read_csv(input_file_path)

    # Iterate over the rows and download historical data for each stock
    for index, row in stock_df.iterrows():
        stock_symbol = row['symbols']  # Assuming 'Symbol' is the column with stock symbols
        output_filename = f"{stock_symbol}.csv"
        
        try:
            download_save_stock_data(stock_symbol, output_filename)
            print(f"Downloaded and saved data for {stock_symbol} to {output_filename}")
        except Exception as e:
            print(f"Error downloading data for {stock_symbol}: {str(e)}")
