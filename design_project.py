# design_project.py
# ENDG 233 F24
# STUDENT NAME(S): Ambrose KhunLee, Max Boucher
# GROUP NAME: The Sigmas
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.

# Import Modules #

import user_csv
import numpy as np
import matplotlib.pyplot as plt

# Define Functions #

# User Prompting Functions

def get_option(options):
    """
    Prints menu of options and prompts user to select one. The selected option number is returned.

    Parameters:
        options (list): List of options for the user to choose from.

    Returns:
        int: The number corresponding to the selected option.
    """
    option_numbers = [] # Initialize list of option numbers as strings

    # Print a menu of the provided options
    for (index, item) in enumerate(options, 1): # For each option
        print(f"\t{index}. {item}") # Print the option number and option
        option_numbers.append(str(index)) # Add the option number as a string to `option_numbers`

    while True: # Continue until a valid input is received
        user_input = input(">> ") # Prompt user
        print() # Print a new line
        if (user_input in option_numbers): # If the users input is valid
            return int(user_input) # Return the user input as an integer
        else: # If the user input is invalid
            print("Error. Invalid input. Please enter the option number.") # Print error message

def get_yes_no_option():
    """
    Prompts user to select either Yes or No.
        
    Returns:
        bool: True if the user choses Yes, False if the user choses No.
    """
    while True: # Continue until a valid input is received
        user_input = input(">> ") # Prompt user
        print() # Print a new line
        formatted_input = user_input.strip() # Remove leading and trailing whitespaces
        formatted_input = user_input.upper() # Convert all characters to uppercase
        if (formatted_input in ["YES", "Y"]): # If the user input is a valid "Yes"
            return True # Return True
        elif (formatted_input in ["NO", "N"]): # If the user input is a valid "No"
            return False # Return False
        else: # If the user input is invalid
            print('Error. Invalid input. Please enter "Yes" or "No".') # Print error message

# Stock/Index Analysis Functions

def avg_daily_prices(data):
    """
    Creates a list of average daily stock/index prices.

    Parameters:
        data (numpy array): The data set of the stock/index for the user selected time range.
    
    Returns:
        list: List of of average daily stock/index prices.
    """
    avg_daily_prices = [] # Initialise a list for the average daily stock prices

    for row in data: # For each day in the data
        avg_daily_price = (row[3] + row[0]) / 2 # Calculate average daily price
        avg_daily_prices.append(avg_daily_price) # Add the average daily price to `avg_daily_prices`

    return avg_daily_prices # Return the `avg_daily_prices` list

def daily_rors(data):
    """
    Calculates the daily rates of returns of a stock/index (RoRs).

    Paramaters:
        data (numpy array): The data set of the stock/index for the user selected time range.

    Returns:
        numpy array: Array of the daily rates of return.
    """
    daily_rors_list = [] # Initialize list of daily rates of return as floats

    for row in data: # For each day in the data
        daily_ror = ((row[3] - row[0]) / row[0]) * 100 # Calculate daily rates of return as a percent
        daily_rors_list.append(daily_ror) # Add daily rates of return to `daily_rors_list`

    daily_rors_array = np.array(daily_rors_list) # Convert `daily_rors_list` to an array

    return daily_rors_array # Return the array

def avg_daily_ror(data):
    """
    Calculates the average daily RoR of the stock/index.

    Parameters:
        data (numpy array): The data set of the stock/index for the user selected time range.
    
    Returns:
        numpy float: The average daily rate of return in percent.
    """
    daily_rors_list = daily_rors(data) # Get the daily rates of return list

    return sum(daily_rors_list) / len(daily_rors_list) # Calculate and return average daily RoR

def max_daily_ror(data):
    """
    Finds the maximum daily rate of return of the stock/index.
    
    Parameters:
        data (numpy array): The data set of the stock/index for the user selected time range.
    
    Returns:
        numpy float: The maximum daily rate of return in percent.
    """
    daily_rors_list = daily_rors(data) # Get the daily rates of return list

    return np.max(daily_rors_list) # Find and return the maximum daily rates of return

def min_daily_ror(data):
    """
    Finds the minimum daily rate of return of the stock/index.
    
    Parameters:
        data (numpy array): The data set of the stock/index for the user selected time range.
    
    Returns:
        numpy float: The minimum daily rate of return in percent.
    """
    daily_rors_list = daily_rors(data) # Get the daily rates of return list

    return np.min(daily_rors_list) # Find and return the minimum daily rates of return

def max_price(data):
    """
    Finds the maximum price of the stock/indec.
    
    Parameters:
        data (numpy array): The data set of the stock/index for the user selected time range.
    
    Returns:
        numpy float: The maximum closing price in USD.
    """
    return np.max(data[:, 3]) # Find and return the maximum value from the closing prices

def min_price(data):
    """
    Finds the minimum price of the stock/index.

    Parameters:
        data (numpy array): The data set of the stock/index for the user selected time range.
    
    Returns:
        numpy float: The minimum closing price in USD.
    """
    return np.min(data[:, 3]) # Find and return the minimum value from the closing prices

def total_ror(data):
    """
    Calculates the total rate of return of the stock/index.

    Paramaters:
        data (numpy array): The data set of the stock/index for the user selected time range.

    Returns:
        numpy float: The total rate of return in percent.
    """
    initial_price = data[-1][3] # Find the closing price from the most recent date (Nov 20th)
    final_price = data[0][3] # Find the closing price from the oldest date within the user selected time range
    return ((final_price - initial_price) / initial_price) * 100 # Calculate and return the total rate of return

def roi(data):
    """
    Calculates the return on an investment (ROI) of $100,000 (AKA the total profit one would make 
    over the user selected time range).

    Paramaters:
        data (numpy array): The data set of the stock/index for the user selected time range.

    Returns:
        numpy float: The return on an investment on $100k in USD.
    """
    return (100000 * (total_ror(data) / 100)) # Calculate and return the return on investment on $100k

def avg_volume(data):
    """
    Calculates the average trading volume of the stock.

    Paramaters:
        data (numpy array): The data set of the stock/index for the user selected time range.

    Returns:
        numpy float: The average tading volume.
    """
    return np.mean(data[:, 4]) # Return the mean of the volume

def alpha(stock_data, spx_data):
    """
    Calculates the alpha value (a type of stock indicator) of the stock compared to the S&P 500.

    Paramaters:
        stock_data (numpy array): The data set of the stock for the user selected time range.
        spx_data (numpy array): The data set of the S&P 500 for the user selected time range.

    Returns:
        numpy float: The alpha value of the stock.
    """
    stock_ror = total_ror(stock_data) / 100 # Get the total rate of return for the stock as a decimal (not a %)
    spx_ror = total_ror(spx_data) / 100 # Get the total rate of return for the S&P 500 as a decimal
    beta_calc = beta(stock_data, spx_data) # Calculate the beta value
    return stock_ror - 0.02 - beta_calc * (spx_ror - 0.02) # Calculate and return the alpha value using a 2% risk free rate of return

def beta(stock_data, spx_data):
    """
    Calculates the beta value (a type of stock indicator) of the stock compared to the S&P 500.

    Paramaters:
        stock_data (numpy array): The data set of the stock for the user selected time range.
        spx_data (numpy array): The data set of the S&P 500 for the user selected time range.

    Returns:
        numpy float: The beta value of the stock.
    """
    stock_rors = daily_rors(stock_data) # Get the daily rates of return array of the stock
    spx_rors = daily_rors(spx_data) # Get the daily rates of return array of the S&P 500
    return np.cov(stock_rors, spx_rors)[0][1] / np.var(spx_rors) # Calculate the beta value (uses sample covariance)

# Print Functions

def print_divider(char, length, extra_line = True):
    """
    Prints a divider composed of a given character and of a specified length.

    Parameters:
        char (str): Character to repeat.
        length (int): Number of times the character will appear.
        extra_line (bool, optional): Whether to print an extra line below the divider. Defaults to True.
    
    Returns:
        None: This function does not return any value.
    """

    divider = "" # Initialise empty string for the divider
    for i in range(length): # For the length of the divider
        divider += char # Add the provided character to the divider
    print(divider) # Print the divider
    if extra_line: # If `extra_line` is True, print an additional newline
        print() # Print extra line

def print_table(data):
    """
    Prints a table reflecting the data of a 2D list.

    Parameters:
        data (list): 2D list to print in a table format.

    Returns:
        None: This function does not return any value.
    """
    for (i, row) in enumerate(data): # For each row in a 2D list
        table_row = "" # Iniitialize empty string for the table row

        for (j, item) in enumerate(row): # For each item in the row
            if (j == 0): # If it is in the first column
                table_row += f"{item:<25}" # Add formatted value to row
                table_row += " || " # Add thick column seperator to row
            elif (i == 0): # If it is in the first row but not in the first column
                table_row += f"{item:<20}" # Add formatted value to row
            else: # If it is not in the first column or the first row
                if ((item < 0.01) and (item > -0.01)): # If the value is between 0.01 and -0.01
                    table_row += f"{item:>20,.3f}" # Add formatted value to row (rounded to 3 decimal places)
                else: # If the value is not between 0.01 and -0.01
                    table_row += f"{item:>20,.2f}" # Add formatted value to row (rounded to 2 decimal places)


            if (j != 0) and (j != (len(row) - 1)): # If is not in the first column and is not in the last column
                    table_row += " | " # Add column seperator to row

        print(table_row) # Print the table row

        if (i == 0): # If the first row has just been printed
            print_divider("=", len(table_row), False) # Print a thick row seperator
        elif (i != (len(data) - 1)): # If a row has just been printed that is not the first or the last
            print_divider("-", len(table_row), False) # Print a row seperator

    print() # Print a new line

def print_alpha(alpha, stock_name):
    """
    Prints the calculated alpha value for the stock.

    Paramaters:
        alpha (float): The alpha value of the stock. 
        stock_name (str): The name of the stock.

    Returns:
        None: This function does not return any value.
    """
    alpha_percent = alpha * 100 # Convert the alpha value to a percentage
    if alpha > 0: # If alpha is greater than 0
        # Print outperformance percent and alpha
        print(f"{stock_name} outperformed the S&P 500 by {alpha_percent:,.2f}%. | alpha = {alpha:,.2f}\n")
    elif alpha < 0: # If alpha is less than 0
        # Print underperformance percent and alpha
        print(f"{stock_name} underperformed the S&P 500 by {alpha_percent:,.2f}%. | alpha = {alpha:,.2f}\n")
    else: # If alpha is equal to 0
        # Print matching performance and alpha
        print(f"{stock_name} performed the same as the S&P 500. | alpha = {alpha:,.2f}\n")

def print_beta(beta, stock_name):
    """
    Prints the calculated beta value for the stock.

    Paramaters:
        beta (float): The beta value of the stock.
        stock_name (str): The name of the stock.

    Returns:
        None: This function does not return any value.
    """
    percent_change = abs((beta - 1) * 100) # Convert the beta value to a percentage
    if beta > 1: # If beta is greater than 1
        # Print higher volatility percent and beta
        print(f"{stock_name} is more volitile than the S&P 500 by {percent_change:,.2f}%. | beta = {beta:,.2f}\n")
    elif beta < 1: # If beta is less than 1
        # Print lower volatility percent and beta
        print(f"{stock_name} is less volitile than the S&P 500 by {percent_change:,.2f}%. | beta = {beta:,.2f}\n")
    else: # If beta is equal to 1
        # Print matching volatility percent and beta
        print(f"{stock_name} has the same volitility as the S&P 500. | beta = {beta:,.2f}\n")

def print_volume(data, stock_name):
    """
    Prints the average daily trading value for the stock.

    Parameters:
        data (numpy array): The data set of the stock for the user selected time range.
        stock_name (str): The name of the stock.

    Returns:
        None: This function does not return any value.
    """
    print(f"Average daily trading volume for {stock_name} is {avg_volume(data):,.2f}\n") # Print average volume

def print_exit_message():
    """
    Prints the exit message.

    Returns:
        None: This function does not return any value.
    """
    # Print exit message
    print("\nThank you for using StockStacker!\n\n\"Risk comes from not knowing what you’re doing.\" - Warren Buffet")

# Graphing Functions

def price_graphs(stock_prices, spx_prices, stock_name, filename):
    """
    Creates graphs for the prices of both the stock and the S&P 500 over time.

    Parameters:
        stock_prices (list): List of prices for the stock.
        spx_prices (list): List of prices for the S&P 500.
        stock_name (str): The name of the stock.
        filename (str): Name of the .png file to save the graphs.
    
    Returns:
        None: This function does not return any value.
    """
    # Put the price data in chronological order
    stock_prices.reverse()
    spx_prices.reverse()

    plt.figure(figsize = (12, 5)) # Create and set the size of the figure

    plt.subplot(1, 2, 1) # First subplot
    plt.plot(stock_prices, color="orange") # Plot the closing price data of the stock
    plt.title(stock_name) # Set the title
    plt.xlabel("Time (Days)") # Set the label for the x axis
    plt.ylabel("Price (USD)") # Set the label for the y axis
    plt.grid(True) # Display grid
    
    plt.subplot(1, 2, 2) # Second subplot
    plt.plot(spx_prices) # Plot the closing price of the S&P 500
    plt.title("S&P 500 (SPX)") # Set the title
    plt.xlabel("Time (Days)") # Set the label for the x axis
    plt.ylabel("Price (USD)") # Set the label for the y axis
    plt.grid(True) # Display grid
    plt.savefig("final_plots/" + filename) # Save graphs as a .png
    plt.show() # Show the graphs

# Define Constants #

# List of the top five publicly traded companies by market cap
STOCKS = ["Apple (AAPL)", "NVIDIA (NVDA)", "Microsoft (MSFT)", "Amazon (AMZN)", "Alphabet (GOOG)"]

# List of the stock tickers for the top five publicly traded companies by market cap. Indexes match that of `STOCKS`.
STOCK_TICKERS = ["AAPL", "NVDA", "MSFT", "AMZN", "GOOG"]

# List of the filenames for the csv files containing the stock data. Indexes match that of `STOCKS`.
FILENAMES = ["aapl.csv", "nvda.csv", "msft.csv", "amzn.csv", "goog.csv"]

# List of selectible time ranges to view stock data
TIME_RANGES = ["1 Month", "3 Months", "6 Months", "1 Year", "5 Years"]

# List of the number of days corresponding with the selectible time ranges. Indexes match that of `TIME_RANGES`.
TIME_RANGES_IN_DAYS = [30, 90, 180, 365, 1826]

# List of statistics comparing the stock to the S&P 500
STATS = ["Average Daily Return (%)", "Highest Daily Change (%)", "Lowest Daily Change (%)", "Price High ($)", "Price Low ($)", "Rate of Return (%)", "Return on $100k ($)"]

# List of the functions to calculate statistics. Indexes match that of `STATS`.
STATS_FUNCTIONS = [avg_daily_ror, max_daily_ror, min_daily_ror, max_price, min_price, total_ror, roi]

# Main Program #
print("ENDG 233 - Final Project\n")

# Print logo
print("""
   _____ _             _     _____ _             _              
  / ____| |           | |   / ____| |           | |             
 | (___ | |_ ___   ___| | _| (___ | |_ __ _  ___| | _____ _ __  
  \___ \| __/ _ \ / __| |/ /\___ \| __/ _` |/ __| |/ / _ \ '__| 
  ____) | || (_) | (__|   < ____) | || (_| | (__|   <  __/ |    
 |_____/ \__\___/ \___|_|\_\_____/ \__\__,_|\___|_|\_\___|_|    
                                                                                                                          
""")

# Print description of program
print("StockStacker compares the top five publicly traded companies by market cap to the S&P 500.\n")

# Print disclaimers
print("Note that the data has a cutoff date of November 20th. Currency is in USD.\n")

while True: # While the program is running
    print_divider("#", 75) # Print divider

    # Prompt user to select a stock
    print("Select a stock to compare to the S&P 500:")
    selected_stock = get_option(STOCKS)
    stock_name = STOCKS[selected_stock - 1]
    stock_ticker = STOCK_TICKERS[selected_stock - 1]
    stock_filename = FILENAMES[selected_stock - 1]

    # Prompt user to select a time range
    print("Select a time range:")
    selected_range = get_option(TIME_RANGES)
    time_range = TIME_RANGES[selected_range - 1]
    days = TIME_RANGES_IN_DAYS[selected_range - 1]

    print_divider("#", 75) # Print divider

    stock_list = user_csv.read_csv(stock_filename, False) # Read the selected stocks csv file
    filtered_stock_list = stock_list[:days] # Get the rows in the selected time range
    stock_array = np.array(filtered_stock_list) # Create numpy array with the stock data

    spx_list = user_csv.read_csv("spx.csv", False) # Read the S&P 500 csv file
    filtered_spx_list = spx_list[:days] # Get the rows in the selected time range
    spx_array = np.array(filtered_spx_list) # Create numpy array with the S&P 500 data

    stats_list = [["Statistics", stock_name, "S&P 500 (SPX)"]] # Initialise 2D list for statistics

    for (index, item) in enumerate(STATS): # For each statistic in `STATS`
        # Calculate the stat for the stock and the S&P 500 and add it to `stats_list`
        stats_list.append([item, STATS_FUNCTIONS[index](stock_array), STATS_FUNCTIONS[index](spx_array)])
    
    print(f"{stock_name} vs the S&P 500 (SPX) over {time_range} (preceeding Nov 20th, 2024)\n") # Print table title
    print_table(stats_list) # Print table with stock stats

    print_divider("=", 75) # Print divider

    print_alpha(alpha(stock_array, spx_array), stock_name) # Print alpha
    print_beta(beta(stock_array, spx_array), stock_name) # Print beta
    print_volume(stock_array, stock_name) # Print average daily trading volume
    
    # Make template for output file filenames
    output_filename = stock_ticker.lower() + "_vs_spx_" + time_range.lower().replace(" ", "_")

    output_csv_filename = output_filename + ".csv" # Create the output csv filename
    user_csv.write_csv(output_csv_filename, stats_list, True) # Write csv file

    print_divider("#", 75) # Print divider

    # Prompt user whether to display stock/index graphs
    print(f"Would you like to display the stocks charts for {stock_name} and the S&P 500? This will end the program. (y/n):")
    show_graphs = get_yes_no_option()

    if (show_graphs): # If user chose the display stock/index graphs
        print_exit_message() # Print exit message

        output_graph_filename = output_filename + ".png" # Create the output graph filename

        # Create graphs of average daily price over time for both the stock and the S&P 500
        price_graphs(avg_daily_prices(stock_array), avg_daily_prices(spx_array), stock_name, output_graph_filename)
    
    # Prompt user whether to continue the program
    print("Would you like to compare another stock? (y/n):")
    continue_program = get_yes_no_option()

    if (not continue_program): # If user quit
        print_exit_message() # Print exit message

        break # End program