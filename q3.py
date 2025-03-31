'''
This program uses file handling to read a file then 
replace a specific word in the file with another file.
'''
# asking user for the name of the file,
# word to find and replace
file_name = input("Enter the file name: ")
word_to_find = input("Enter the word to find: ")
replacement_word = input("Enter the replacement word: ")

# file handling for replacing word
try:
    with open(file_name, "r") as file:
        content = file.read()
    updated_content = content.replace(word_to_find, replacement_word)

    with open(file_name, "w") as file:
        file.write(updated_content)

    print(f"All occurrences of '{word_to_find}' have been replaced with '{replacement_word}' in {file_name}.")

# error handling
except FileNotFoundError:
    print("Error. The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

