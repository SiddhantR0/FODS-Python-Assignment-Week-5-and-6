'''
This program uses the concept of file handling to read a file 
and ten count the number of lines, words and characters in that
file.
''' 

# file handling part
def count_file_details(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)

        # displaying the output
        print(f"File: {filename}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_chars}")

    # error handling 
    except FileNotFoundError:
        print("Error. The file was not found")
    except Exception as e:
        print(f"An error occurred: {e}")

# asking the user for the name of the file
filename = input("Enter the filename: ")
count_file_details(filename)
