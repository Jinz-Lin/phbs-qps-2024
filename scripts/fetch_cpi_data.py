import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Fetch CPI data for the United States
def fetch_cpi_data():
    start_date = datetime(2010, 1, 1)
    end_date = datetime.today()

    # Retrieve CPI data from FRED (Federal Reserve Economic Data)
    cpi_data = web.DataReader('CPIAUCSL', 'fred', start_date, end_date)
    
    return cpi_data

# Calculate the inflation rate for the past four quarters
def calculate_inflation(cpi_data):
    # Resample the data by quarter and use the last value of each quarter
    cpi_data_quarterly = cpi_data.resample('Q').last()  # Resample to quarterly data
    
    # Calculate quarterly inflation rate (from one quarter to the next)
    inflation = cpi_data_quarterly.pct_change(periods=1) * 100
    
    # Get the inflation data for the last 4 quarters
    inflation_last_4_quarters = inflation.tail(4)
    
    # Add a note for the current quarter about using the latest month's CPI
    current_quarter = inflation_last_4_quarters.index[-1]
    inflation_note = f"Note: Current quarter uses CPI of {cpi_data.index[-1].strftime('%B %Y')}!!!"
    
    return inflation_last_4_quarters, inflation_note

# Optional: Plot the inflation data as a bar chart
def plot_inflation(inflation_data):
    inflation_data.plot(kind='bar', title='US Seasonal Inflation Rate (Last 4 Quarters)', figsize=(10,6))
    plt.xlabel('Date')
    plt.ylabel('Seasonal Inflation Rate (%)')
    plt.show()

if __name__ == "__main__":
    cpi_data = fetch_cpi_data()  # Fetch CPI data
    inflation_data, inflation_note = calculate_inflation(cpi_data)  # Calculate inflation rate
    print(inflation_data)  # Print the inflation data for the last 4 quarters
    print(inflation_note)  # Print the note for the current quarter
    plot_inflation(inflation_data)  # Visualize the inflation rate
