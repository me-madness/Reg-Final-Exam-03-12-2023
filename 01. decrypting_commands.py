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
        message[start_index:end_index:]
    elif command[0] == "Make":
        case_lower_upper = command[1]
        if case_lower_upper == "Upper":
            message = message.upper()
            print(f"{message}")
        else:
            message = message.lower()
            print(f"{message}")    
    elif command[0] == "Check":
        find_word = command[1]
        if message.find(find_word):
            print(f"Message contains {find_word}")
        else:
            print(f"Message doesn't contain {find_word}")    
    elif command[0] == "Sum":
        start_index = command[1]
        end_index = command[2]
    command = input().split(' ')    
    
    
# ILikeSoftUni
# Replace I We
# Make Upper
# Check SoftUni
# Sum 1 4
# Cut 1 4
# Finish

