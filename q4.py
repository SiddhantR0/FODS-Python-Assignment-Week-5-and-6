'''
This program reads a csv file and then displays the content
of the csv file in a tabular format.
'''

# importing csv 
# and tabulate module using pip
import csv
from tabulate import tabulate 

# file handling part 
def read_csv_and_display(file_name):
    try:
        with open(file_name, newline='') as file:
            reader = csv.reader(file)
            data = list(reader)  
        if data:
            print(tabulate(data, headers="firstrow", tablefmt="grid"))  
        else:
            print("The file is empty.")

    # error handling
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# asking the user for name of the file
file_name = input("Enter the CSV file name: ")
read_csv_and_display(file_name)
