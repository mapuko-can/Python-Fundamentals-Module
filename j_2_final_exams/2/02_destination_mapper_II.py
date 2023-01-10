import re

places = input()

valid_locations = []
travel_points = 0

pattern = r"([=\/])([A-Z][A-Za-z]{2,})(\1)"

matches = re.findall(pattern, places)

for match in matches:
    valid_locations.append(match[1])

for location in valid_locations:
    travel_points += len(location)

print(f'Destinations: {", ". join(valid_locations)}')
print(f"Travel Points: {travel_points}")