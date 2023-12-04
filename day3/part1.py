import string

lines_text=[]
with open("text.txt", "r") as f:
    for x in f:
        lines_text.append(x.strip())  # Using strip() to remove newline characters

final = []

def is_adjacent_to_symbol(lines, line_index, start_index, end_index): #whole,0,9,11
    # Check in the current line
    if start_index > 0 and lines[line_index][start_index - 1] not in string.digits + '. ': #check before
        return True
    if end_index < len(lines[line_index]) and lines[line_index][end_index] not in string.digits + '. ': #check after
        return True

    # Check above and below
    for i in [line_index - 1, line_index + 1]: #1
        if 0 <= i < len(lines): #true
            for j in range(start_index - 1, end_index + 1): #[0,3]
                if 0 <= j < len(lines[i]) and lines[i][j] not in string.digits + '. ': #0
                    return True

    return False

for line_index, line in enumerate(lines_text): #0
    current_number = ''
    num_start_index = 0

    for char_index, char in enumerate(line): #11
        if char.isdigit(): 
            current_number += char 
            if len(current_number) == 1: 
                num_start_index = char_index #9
        else:
            if current_number: #43
                num_end_index = char_index #11
                if is_adjacent_to_symbol(lines_text, line_index, num_start_index, num_end_index): #whole,0,9,11
                    final.append(int(current_number))
            current_number = ''

    # Check the last number in the line
    if current_number:
        num_end_index = len(line)
        if is_adjacent_to_symbol(lines_text, line_index, num_start_index, num_end_index):
            final.append(int(current_number))

print(final)
