import yfinance as yf
import pandas as pd

# Define a dictionary of stock symbols and their corresponding file names
stock_data = {
    'AAPL': 'apple_data.csv',
    'MSFT': 'microsoft_data.csv',
    'GOOGL': 'alphabet_data.csv',
    'AMZN': 'amazon_data.csv',
    'META' : 'facebook_data.csv',
    'PLD' : 'prologis_data.csv',
    'EQR' : 'equity_data.csv',
    'SPG' : 'simon_data.csv',
    'PSA' : 'public_data.csv',
    'AVB' : 'avalonbay_data.csv',
    'PSO' : 'pearson_data.csv',
    'ATGE' : 'adtalem_data.csv',
    'STRA' : 'strategic_data.csv',
    'CHGG' : 'chegg_data.csv',
    'LOPE' : 'grand_data.csv',
    'JNJ' : 'jhonson_Data.csv',
    'PFE':'pfizer_data.csv',
    'UNH' : 'united_data.csv',
    'MRK':'merck_data.csv',
    'AMGN':'amgen_data.csv',
    'BHP':'bhp_data.csv',
    'RIO':'rio_data.csv',
    'FCX':'freeport_data.csv',
    'NEM':'newmont_Data.csv',
    'VALE':'vale_data.csv',
    'XOM':'exxon_data.csv',
    'CVX':'chevron_data.csv',
    'COP':'conoco_data.csv',
    'KMI':'kinder_data.csv',
    'D':'dominion_data.csv',
    'WMT':'walmart_data.csv',
    'HD':'home_data.csv',
    'COST':'costco_data.csv',
    'TGT':'target_data.csv',
    'KO':'coca_data.csv',
    'PEP':'pepsi_data.csv',
    'TSN':'tyson_data.csv',
    'MCD':'mcd_data.csv',
    'ADM':'archer_data.csv',
    'JPM':'jp_data.csv',
    'BAC':'bankamerica_data.csv',
    'WFC':'wells_data.csv',
    'C':'citi_data.csv',
    'GS':'goldman_data.csv',
    'INTC':'intel_data.csv',
    'NVDA':'nvidia_data.csv',
    'AMD':'amd_data.csv',
    'TSM':'taiwan_data.csv',
    'AMAT':'applied_data.csv',
    'GM':'general_data.csv',
    'F':'ford_data.csv',
    'TSLA':'tesla_data.csv',
    'HMC':'honda_data.csv',
    'CRM':'sales_data.csv',
    'ADBE':'adobe_data.csv',
    'SHOP':'shopify_data.csv',
    'SSNLF':'samsung_data.csv',
    'PCRFY':'panasonic_data.csv'
    
}

# Define the time period
start_date = pd.Timestamp.now() - pd.DateOffset(years=2)
end_date = pd.Timestamp.now()

# Loop through the stock data dictionary
for symbol, filename in stock_data.items():
    # Download historical data for the current stock symbol
    df = yf.download(symbol, start=start_date, end=end_date)
    
    # Display the downloaded data
    print(f'Downloaded data for {symbol}:')
    
    
    # Save the data to a separate CSV file
    df.to_csv(filename)

# The data for each stock will be saved in separate CSV files with their respective filenames.
