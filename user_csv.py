# user_csv.py
# ENDG 233 F24
# STUDENT NAME(S): Ambrose KhunLee, Max Boucher
# GROUP NAME: The Sigmas
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.

def read_csv(filename, include_headers = True):
    """
    Reads a csv file and returns its content as a 2D list.

    Parameters:
        filename (str): The name of the file from which to read data from.
        include_headers (bool, optional): Whether to include headers in the returned data. Defaults to True.

    Returns:
        list: A 2D list representing the contents of the csv file. Each inner list corresponds to a row of the csv file.
    """

    file = open(("data_files/" + filename), "r") # Open csv file

    string_data = [] # Initialise a list for the csv data with string values

    for line in file: # For each line in the csv file
        row = line.replace("\n", "") # Remove all newline escape characters
        row = row.split(",") # Turn the comma seperated string into a list
        row = row[1:] # Slice the list to remove the date
        string_data.append(row) # Add row to the `string_data` 2D list

    file.close() # Close csv file

    headers = string_data[0] # Get the header row

    string_data.pop(0) # Remove the header row

    string_data.reverse() # Put the data in reverse chronological order

    float_data = [] # Initialise a list for the csv data with float values

    for row in string_data: # For each row in the `string_data` 2D list
        float_row = [] # Initialise a list for the row with floats
        for item in row: # For each item in the `float_row` list
            if (item == ""): # If value is empty
                float_row.append(0) # Add 0 to the `float_row` list
            else: # If value is not empty
                float_row.append(float(item)) # Add the item as a float to the `float_row` list
        float_data.append(float_row) # Add the row to the `float_data` 2D list

    if include_headers: # If the `include_headers` parameter is True
        float_data.insert(0, headers) # Add the `headers` row to the `float_data`

    return float_data # Return the `float_data` 2D list reflecting the csv file data

def write_csv(filename, data, overwrite):
    """
    Writes provided data in the form of a 2D list to a cvs file.

    Parameters: 
        filename (str): The name of the csv file to write to.
        data (list): The 2D list used to write to the csv file.
        overwrite (bool): Whether to overwrite the existing csv file.
    
    Returns:
        None: This function does not return any value.
    """
    if overwrite: # If the `overwrite` parameter is True
        file = open(("data_files/" + filename), "w") # Open csv file to overwite the data
    else: # If `overwrite` parameter is False
        file = open(("data_files/" + filename), "a") # Open csv file to append new data

    for row in data: # For each row in the provided data
        for i in range(len(row)): # For the index of each items in the row
            file.write(str(row[i])) # Write the corresponding entry to the csv file
            if (i < len(row) - 1): # If the corresponding entry is not the last in the row
                file.write(",") # Write a comma to the csv file
        file.write("\n") # Add a new line to the csv file
        
    file.close() # Close csv file
