import re

locations = input()
valid_destinations = []
travel_points = 0

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
matches = re.finditer(pattern, locations)

for match in matches:
    valid_destinations.append(match.group(2))
for destination in valid_destinations:
    travel_points += len(destination)

print(f'Destinations: {", ".join(valid_destinations)}')
print(f"Travel Points: {travel_points}")

# import re
#
# data = input()
# pattern = r'(=|\/)[A-Z][A-Za-z]{2,}\1'
# result = re.finditer(pattern, data)
#
# points = 0
# all_destinations = []
#
# for destination in result:
#     current_destination = re.split('\/|=', destination.group())[1]
#     points += len(current_destination)
#     all_destinations.append(current_destination)
#
# print(f"Destinations: {', '.join(all_destinations)}")
# print(f"Travel Points: {points}")
