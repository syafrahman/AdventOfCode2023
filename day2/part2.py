import re

lines_text=[]

with open("text.txt", "r") as f:
    for x in f:
        lines_text.append(x.strip())  # Using strip() to remove newline characters

pattern = r'(\d+) (red|blue|green)'
final_data= []
game_id =[]
sum = 0

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
    red = 0
    blue = 0
    green = 0
    for set in range(len(game)):
        if game[set][0] > red:
            red = game[set][0]
        if game[set][1] > blue:
            blue = game[set][1]
        if game[set][2] > green:
            green = game[set][2]
    sum += red*blue*green
        
print(sum)

# import re

# pattern = r'(\d+) (red|blue|green)'

# def process_line(line):
#     color_counts = {'red': 0, 'blue': 0, 'green': 0}
#     for number, color in re.findall(pattern, line):
#         color_counts[color] = max(color_counts[color], int(number))
#     return color_counts['red'] * color_counts['blue'] * color_counts['green']

# with open("text.txt", "r") as f:
#     total_sum = sum(process_line(line.strip()) for line in f)

# print(total_sum)
