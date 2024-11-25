# PHBS QPS 2024

This repository contains code to fetch U.S. Consumer Price Index (CPI) data and calculate the inflation rate for the last four quarters.

## Repository Link
[GitHub Repository Link](https://github.com/Jinz-Lin/phbs-qps-2024)

## Project Description

This project fetches U.S. Consumer Price Index (CPI) data from FRED (Federal Reserve Economic Data) and calculates the inflation rate for the last four quarters. The inflation rate is computed using the Year-Over-Year Change for each quarter and visualized using bar charts.

## Requirements

- Python 3.x
- Required Python libraries: `pandas`, `pandas_datareader`, `matplotlib`

## Setup and Run Instructions

### Setup Steps

1. Clone the repository:
   git clone https://github.com/Jinz-Lin/phbs-qps-2024.git

2. Navigate to the project directory:
   cd phbs-qps-2024

3. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate

4. Install the required dependencies:
   pip install pandas pandas_datareader matplotlib

### Running the Code

1. Navigate to the scripts/ directory:
   cd scripts/

2. Run the script to fetch CPI data and calculate inflation:
   python fetch_cpi_data.py

## Folder Structure

phbs-qps-2024/

├── data/          # Data folder (currently empty)

├── notebooks/     # Jupyter notebooks (optional)

├── scripts/       # Python scripts folder

│   └── fetch_cpi_data.py  # Script to fetch CPI data and calculate inflation

├── src/           # Source code folder (optional)

├── requirements.txt  # Project dependencies file

└── README.md      # Project README file

## License

This project is licensed under the MIT License - see the LICENSE file for details.


