import pyperclip
import os

user_input = ""
try:
    while user_input != "exit":
        user_input = input("Enter the text:\n")
        os.system('cls')
        result_str = ""
        for index in range(0, len(user_input)):
            if index > 0 and index < len(user_input) - 1 and user_input[index] == ".":
                if user_input[index - 1].isnumeric() and user_input[index + 1].isnumeric():
                    result_str += ','
                else:
                    result_str += user_input[index]
            else:
                result_str += user_input[index]

        if len(user_input.split()) > 0 and user_input.split()[0] != "exit":
            pyperclip.copy(result_str)
            print("The string was copied to the clipboard")
except Exception as e:
    print(f"An error occurred: {e}")


