'''
This program copies the content of one file then pastes that 
content into another file.
'''

# asking user for name of the files.
source_file = input("Enter the name of the file you want to copy from: ")
destination_file = input("Enter the name of the file you want to paste in: ")

# copy paste code (read and write)
try:
    with open(source_file, "r") as src:
        content = src.read()
        
    with open(destination_file, "w") as dest:
        dest.write(content)
        
    print(f"Contents successfully copied from {source_file} to {destination_file}.")

# error handling
except FileNotFoundError:
    print("Error. The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

