import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Fetch the US CPI data from FRED (Federal Reserve Economic Data)
def fetch_cpi_data():
    start_date = datetime(2010, 1, 1)
    end_date = datetime.today()

    # CPI data from FRED
    cpi_data = web.DataReader('CPIAUCSL', 'fred', start_date, end_date)
    
    return cpi_data

# Calculate inflation for the last 4 quarters
def calculate_inflation(cpi_data):
    # Quarterly data: Use pct_change() with periods=3 for year-over-year inflation
    inflation = cpi_data.pct_change(periods=3) * 100
    return inflation.tail(4)  # Last 4 quarters

# Plot inflation data for visualization (optional)
def plot_inflation(inflation_data):
    inflation_data.plot(kind='bar', title='US Inflation (Last 4 Quarters)', figsize=(10,6))
    plt.xlabel('Date')
    plt.ylabel('Inflation (%)')
    plt.show()

if __name__ == "__main__":
    cpi_data = fetch_cpi_data()
    inflation_data = calculate_inflation(cpi_data)
    print(inflation_data)
    plot_inflation(inflation_data)
