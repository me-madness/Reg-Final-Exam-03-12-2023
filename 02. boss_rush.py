import re

input_lines = int(input())
pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+[\ ]{1}[A-Za-z]+)#"


for line in range(input_lines):
    current_input = input()
    match = re.fullmatch(pattern, current_input)
    
    if match:
        boss_name = match[1]
        title = match[2]
    else:
        print(f"Access denied!")    

# 3
# |PETER|:#Lead architect#
# |GEORGE|:#High Overseer#
# |ALEX|:#Assistant Game Developer#

    