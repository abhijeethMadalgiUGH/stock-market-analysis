import pandas as pd
import numpy as np
import ta
from yfinance import Ticker
import os

def process_stock_data(stock_symbol):
    # Replace 'your_data_directory' with the actual path to your data directory
    data_directory = 'C:/Users/devar/OneDrive/Desktop/dev/Product'
    
    # Construct the file name based on the stock symbol
    filename = os.path.join(data_directory, f"{stock_symbol}.csv")

    try:
        # Check if the file exists before processing
        if os.path.exists(filename):
            # Add your processing logic here
            print(f"Processing data for {stock_symbol} from {filename}")
            # Example: Read the data using pandas
            data = pd.read_csv(filename)
            # Calculate Moving Averages (SMA and EMA)
            data['SMA_50'] = ta.trend.sma_indicator(data['Close'], window=50)
            data['SMA_200'] = ta.trend.sma_indicator(data['Close'], window=200)
            data['EMA_12'] = ta.trend.ema_indicator(data['Close'], window=12)
            data['EMA_26'] = ta.trend.ema_indicator(data['Close'], window=26)

            # Calculate RSI
            data['RSI'] = ta.momentum.rsi(data['Close'], window=14)

            # Calculate MACD
            data['MACD'] = ta.trend.macd(data['Close'], window_fast=12, window_slow=26)
            data['MACD_Signal'] = ta.trend.macd_signal(data['Close'], window_fast=12, window_slow=26)

            # Calculate Bollinger Bands
            window = 20
            sma = data['Close'].rolling(window=window).mean()
            std = data['Close'].rolling(window=window).std()
            data['Bollinger_Bands'] = sma + 2 * std
            data['Bollinger_Bands_Lower'] = sma - 2 * std

            # Calculate Average True Range (ATR)
            data['ATR'] = ta.volatility.average_true_range(data['High'], data['Low'], data['Close'], window=14)

            # Calculate Fibonacci Retracement levels
            data['Fibonacci_0.236'] = data['Close'].shift(1) + (0.236 * (data['High'].shift(1) - data['Low'].shift(1)))
            data['Fibonacci_0.382'] = data['Close'].shift(1) + (0.382 * (data['High'].shift(1) - data['Low'].shift(1)))
            data['Fibonacci_0.618'] = data['Close'].shift(1) + (0.618 * (data['High'].shift(1) - data['Low'].shift(1)))

            # Calculate Volume Analysis
            data['Volume_MA'] = data['Volume'].rolling(window=14).mean()

            # Calculate On-Balance Volume (OBV)
            obv = [0]
            for i in range(1, len(data)):
                if data['Close'].iloc[i] > data['Close'].iloc[i - 1]:
                    obv.append(obv[-1] + data['Volume'].iloc[i])
                elif data['Close'].iloc[i] < data['Close'].iloc[i - 1]:
                    obv.append(obv[-1] - data['Volume'].iloc[i])
                else:
                    obv.append(obv[-1])
            data['OBV'] = obv

            # Volume Weighted Average Price (VWAP)
            data['VWAP'] = ta.volume.volume_weighted_average_price(data['High'], data['Low'], data['Close'], data['Volume'])

             # Average Directional Index (ADX)
            data['ADX'] = ta.trend.adx(data['High'], data['Low'], data['Close'], window=14)

            # Commodity Channel Index (CCI)
            data['CCI'] = ta.trend.cci(data['High'], data['Low'], data['Close'], window=20)

            # Williams %R
            data['WilliamsR'] = ta.momentum.WilliamsRIndicator(high=data['High'], low=data['Low'], close=data['Close'], lbp=14).williams_r()

            # Ichimoku Cloud
            ichimoku = ta.trend.IchimokuIndicator(high=data['High'], low=data['Low'])
            data['IchimokuCloud_Base'] = ichimoku.ichimoku_base_line()
            data['IchimokuCloud_Conversion'] = ichimoku.ichimoku_conversion_line()
            data['IchimokuCloud_Lag'] = ichimoku.ichimoku_a()

            # Aroon Oscillator
            aroon_indicator = ta.trend.AroonIndicator(close=data['Close'], window=25)
            data['AroonOscillator'] = aroon_indicator.aroon_indicator()

            # Rate of Change (ROC)
            data['ROC'] = ta.momentum.roc(data['Close'], window=12)

            # Money Flow Index (MFI)
            data['MFI'] = ta.volume.money_flow_index(data['High'], data['Low'], data['Close'], data['Volume'], window=14)

            # Elder Ray Index
            data['EMA_20'] = ta.trend.ema_indicator(data['Close'], window=20)
            data['BullPower'] = data['High'] - data['EMA_20']
            data['BearPower'] = data['Low'] - data['EMA_20']

            # Triangular Moving Average (TMA)
            data['TMA'] = ta.trend.trix(data['Close'], window=15)

            # Chande Momentum Oscillator (CMO)
            data['CMO'] = ta.trend.cci(data['High'], data['Low'],data['Close'], window=14)

            # Ease of Movement (EMV)
            data['EMV'] = ta.volume.ease_of_movement(data['High'], data['Low'], data['Close'], data['Volume'])

            # Price Rate of Change (PROC)
            data['PROC'] = ta.momentum.roc(data['Close'], window=10)


            # Donchian Channels
            donchian_bands = ta.volatility.BollingerBands(data['Close'], window=20, window_dev=2)
            data['Donchian_LowerBand'] = donchian_bands.bollinger_lband()
            data['Donchian_UpperBand'] = donchian_bands.bollinger_hband()

            # Your additional processing logic goes here
        else:
            print(f"Data file for {stock_symbol} not found: {filename}")
    except Exception as e:
        print(f"Error processing data for {stock_symbol}: {str(e)}")



    
    # Save the updated data to the same CSV file
    data.to_csv(f"{stock_symbol}.csv", index=False)
    print("Technical Indicators added successfully")
    
if __name__ == "__main__":
    # Replace 'your_input_file.csv' with the actual path to your CSV file
    input_file_path = 'output_stockerbot_embed_cleaned.csv'

    # Read the CSV file using pandas
    stock_df = pd.read_csv(input_file_path)

    # Iterate over the rows and process data for each stock
    for index, row in stock_df.iterrows():
        stock_symbol = row['symbols']  # Assuming 'Symbol' is the column with stock symbols
        process_stock_data(stock_symbol)

