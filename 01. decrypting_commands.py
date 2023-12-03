message = input()
command = input().split(' ')

while command[0] != "Finish":
    if command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        new_message = message.replace(current_char, new_char)
        print(f"{new_message}")
    elif command[0] == "Cut":
        pass
    elif command[0] == "Make":
        pass
    elif command[0] == "Check":
        pass
    elif command[0] == "Sum":
        pass
    
    
# ILikeSoftUni
# Replace I We
# Make Upper
# Check SoftUni
# Sum 1 4
# Cut 1 4
# Finish

