message = input()
command = input().split(' ')

while command[0] != "Finish":
    if command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        message = message.replace(current_char, new_char)
        print(f"{message}")
    elif command[0] == "Cut":
        start_index = command[1]
        end_index = command[2]
    elif command[0] == "Make":
        case_lower_upper = command[1]
        if case_lower_upper == "Upper":
            print(f"{message.upper()}")
        else:
            print(f"{message.lower()}")    
    elif command[0] == "Check":
        pass
    elif command[0] == "Sum":
        start_index = command[1]
        end_index = command[2]
    
    
# ILikeSoftUni
# Replace I We
# Make Upper
# Check SoftUni
# Sum 1 4
# Cut 1 4
# Finish

