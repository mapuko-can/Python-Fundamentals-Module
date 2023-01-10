import re

text = input()

pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2,2}\/\d{2,2}\/\d{2,2})\1(\d{1,5})\1'
matches = re.finditer(pattern, text)
list_of_matches = []
total_calories = 0
for match in matches:
    list_of_matches.append([match.group(2), match.group(3), match.group(4)])
    total_calories += int(match.group(4))
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for match in list_of_matches:
    print(f"Item: {match[0]}, Best before: {match[1]}, Nutrition: {match[2]}")