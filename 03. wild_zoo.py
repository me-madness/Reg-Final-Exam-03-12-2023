command = input().split(":")
animals = {}

while command != "EndDay":
    message = command[1].split("-")
    print(message)
    if command[0] == "Add":
        animal_name = message[0]
        needed_food_quantity = message[1]
        area = message[2]
    if command[0] == "Feed":
        food = message[1]   
    
    command = input().split(":")
# Add: Adam-4500-ByTheCreek
# Add: Maya-7600-WaterfallArea
# Add: Maya-1230-WaterfallArea
# Feed: Jamie-2000
# EndDay
    