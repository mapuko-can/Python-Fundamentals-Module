import re

text = input()

pattern = r"([#|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
matches = re.finditer(pattern, text)
foods = []
total_calories = 0

for match in matches:
    foods.append([match[2], match[3], match[4]])
    total_calories += int(match[4])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for food in foods:
    print(f"Item: {food[0]}, Best before: {food[1]}, Nutrition: {food[2]}")


# import re
#
# data = input()
#
# pattern = r"([#\|])(?P<item>[a-zA-Z\s]+)\1(?P<exp_date>\d{2}/\d{2}/\d{2})\1(?P<calories>([0-9][0-9]{0,3}|10000))\1"
#
# valid_data = re.finditer(pattern, data)
# food_data = []
# total_calories = 0
# calories_per_day = 2000
#
# for match in valid_data:
#     food_data.append(match.groupdict())
#     calories = int(match["calories"])
#     total_calories += calories
#
# print(f"You have food to last you for: {total_calories // calories_per_day} days!")
# for el in food_data:
#     print(f"Item: {el['item']}, Best before: {el['exp_date']}, Nutrition: {el['calories']}")