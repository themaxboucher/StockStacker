# StockStacker 📉📈

StockStacker is a Python-based terminal program designed to analyze and visualize stock market data. Created as part of the ENDG 233 course (Fall 2024) at the University of Calgary, this project compares the performance of the top five publicly traded companies (by market capitalization) against the S&P 500. The program provides insights into average prices, rates of return, volatility metrics, and investment performance through statistical calculations and visualizations.

## Features
- **Stock Data Analysis**:
  - Calculate average daily prices and rates of return.
  - Identify maximum and minimum prices and rates of return.
  - Evaluate total and average rates of return.
  - Compute alpha and beta values for stock performance.
  - Analyze average daily trading volume.

- **Graphical Visualizations**:
  - Generate side-by-side graphs comparing stock prices to the S&P 500 over time.

- **Interactive Terminal Interface**:
  - User-friendly prompts for selecting options and timeframes.
  - Detailed outputs presented in well-formatted tables.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `numpy` for numerical operations.
  - `matplotlib` for graph plotting.
  - Custom module: `user_csv` for handling CSV files.

## How It Works
1. The user selects a stock and specifies a timeframe for analysis.
2. The program processes historical data to compute various performance metrics.
3. Results are displayed in the terminal, including formatted tables and insights.
4. Graphs comparing stock performance to the S&P 500 are generated and saved as `.png` files.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-github-username>/StockStacker.git
   cd StockStacker
   ```
2. Install the required Python libraries:
   ```bash
   pip install numpy matplotlib
   ```
3. Ensure `user_csv.py` is present in the project directory for CSV handling.

## Usage
1. Run the program:
   ```bash
   python design_project.py
   ```
2. Follow the on-screen prompts to:
   - Select a stock to analyze.
   - Specify a timeframe for analysis.
   - View results and graphs.
3. Access saved graphs in the `final_plots` directory.

## Example Output
  ```
###########################################################################

NVIDIA (NVDA) vs the S&P 500 (SPX) over 5 Years (preceeding Nov 20th, 2024)

Statistics                || NVIDIA (NVDA)        | S&P 500 (SPX)       
========================================================================
Average Daily Return (%)  ||                 0.08 |                 0.02
------------------------------------------------------------------------
Highest Daily Change (%)  ||                13.01 |                 5.49
------------------------------------------------------------------------
Lowest Daily Change (%)   ||               -10.55 |                -5.71
------------------------------------------------------------------------
Price High ($)            ||               148.88 |             6,001.35
------------------------------------------------------------------------
Price Low ($)             ||                 3.15 |             2,237.40
------------------------------------------------------------------------
Rate of Return (%)        ||             3,611.97 |               143.67
------------------------------------------------------------------------
Return on $100k ($)       ||         3,611,968.16 |           143,665.92

===========================================================================

NVIDIA (NVDA) outperformed the S&P 500 by 3,353.76%. | alpha = 33.54

NVIDIA (NVDA) is more volitile than the S&P 500 by 80.85%. | beta = 1.81

Average daily trading volume for NVIDIA (NVDA) is 473,379,977.67

###########################################################################     
  ```

## Team Members
- **Ambrose KhunLee**
- **Max Boucher**

