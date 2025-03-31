'''
In this program various modules are used to count the
number of occurance of each word in a file that is 
specified by the user.
'''

# importing string module for handling punctuation
import string

# importing Counter for word counting
from collections import Counter

# function for counting occurant of each word in a file
def count_word_occurrences(file_name):

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            # removing punctuations
            text = file.read().lower().translate(str.maketrans("", "", string.punctuation)) 
            # counting occurrences
            word_count = Counter(text.split()) 

        if word_count:
            print("\nWord Count in the File:")
            for word, count in sorted(word_count.items()):
                print(f"{word}: {count}")
        else:
            print("The file is empty.")

    # error handling
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# asking the user for name of the file
file_name = input("Enter the text file name: ")
count_word_occurrences(file_name)
