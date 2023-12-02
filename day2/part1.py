import re

lines_text=[]

with open("text.txt", "r") as f:
    for x in f:
        lines_text.append(x.strip())  # Using strip() to remove newline characters

pattern = r'(\d+) (red|blue|green)'
final_data= []
game_id =[]

for line_ in lines_text:
    sets = line_.split(';')
    extracted_data = []
    for set_ in sets:
        
        matches = re.findall(pattern, set_)

        color_counts = {'red': 0, 'blue': 0, 'green': 0}
        
        for match in matches:
            color_counts[match[1]] = int(match[0])

        extracted_data.append((color_counts['red'], color_counts['blue'], color_counts['green']))
    final_data.append(extracted_data)

for index, game in enumerate(final_data):
    for set in range(len(game)):
        if game[set][0] > 12:
            game_id.append(index+1)
            break
        elif game[set][1] > 14:
            game_id.append(index+1)
            break
        elif game[set][2] > 13:
            game_id.append(index+1)
            break

print(5050-sum(game_id))

# import re

# pattern = r'(\d+) (red|blue|green)'

# game_id = []

# with open("text.txt", "r") as f:
#     for index, line in enumerate(f):
#         sets = line.strip().split(';')
#         for set_ in sets:
#             color_counts = {'red': 0, 'blue': 0, 'green': 0}
#             if color_counts['red'] > 12 or color_counts['blue'] > 14 or color_counts['green'] > 13:
#                 game_id.append(index + 1)
#                 break  # Exit the inner loop as soon as a condition is met

# print(5050 - sum(game_id))

