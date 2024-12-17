import pyperclip

user_input = ""
while(user_input != "exit"):
    user_input = input("Enter the text:\n")
    result_str = ""
    for index in range(0, len(user_input)):
        if (index > 0 and index < len(user_input) - 1 and user_input[index] == "."):
            if (user_input[index - 1].isnumeric() and user_input[index + 1].isnumeric()):
                result_str += ','
            else:
                result_str += user_input[index]
        else:
            result_str += user_input[index]
    if (user_input != "exit"):
        pyperclip.copy(result_str)
        print(f"The string was copied to the clipboard")


