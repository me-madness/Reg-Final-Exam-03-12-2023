message = input()
command = input()

while command != "Finish":
    command = input().split(' ')
    if command == "Replace":
        current_char = command[1]
        new_char = command[2]
        new_message = message.replace(current_char, new_char)
        print(f"{new_message}")
    elif command == "Cut":
        pass
    elif command == "Make":
        pass
    elif command == "Check":
        pass
    elif command == "Sum":
        pass