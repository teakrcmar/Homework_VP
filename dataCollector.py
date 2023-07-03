import yfinance as yf
import datetime

# Stock Symbols
symbols = ['AAPL']

# Set time frame (2000-present)
end_date = datetime.datetime.now().strftime('%Y-%m-%d')
start_date = '2000-01-01'  # Specify the start date

# Downloading data and saving them into separate CSV files
for symbol in symbols:
    data = yf.download(symbol, start=start_date, end=end_date)
    filename = f"{symbol}_Stock_Data.csv"
    data.to_csv(filename)
    
    print(f"Data for {symbol} are saved in {filename}.")
