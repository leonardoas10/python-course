import json
import pickle


# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.
# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.
# 4) Adjust the logic to load the file content to work with pickled/ json data.
while True:
    choice = input('pick 1 for write  - 2 for read - 3 exit')
    if choice == '1':
        write = input('what you want to write?')
        with open('exercise-5.txt', mode='w') as f:
            f.write(json.dumps(write))
    elif choice == '2':
        with open('exercise-5.txt', mode='r') as f:
            file_content = f.readlines()
            print(file_content)
    elif choice == '3':
        break 

