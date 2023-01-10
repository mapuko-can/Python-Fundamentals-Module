number = int(input())
plants = {}


for i in range(number):
    plant, rarity = input().split("<->")
    plants[plant] = {"rarity": rarity, "rating": []}

command = input()
while command != "Exhibition":
    commands = command.split(": ")
    current_command = commands[0]
    other_commands = commands[1].split(" - ")
    current_plant = other_commands[0]
    if current_plant not in plants:
        print("error")
        command = input()
        continue

    if current_command == "Rate":
        rating = int(other_commands[1])
        plants[current_plant]['rating'].append(rating)

    elif current_command == "Update":
        new_rarity = other_commands[1]
        plants[current_plant]['rarity'] = new_rarity

    elif current_command == "Reset":
        plants[current_plant]['rating'].clear()
    command = input()

print("Plants for the exhibition:")

for current_plant in plants:
    if len(plants[current_plant]['rating']) > 0:
        average_rating = sum(plants[current_plant]['rating']) / len(plants[current_plant]['rating'])
    else:
        average_rating = 0.00
    print(f"- {current_plant}; Rarity: {plants[current_plant]['rarity']}; Rating: {average_rating:.2f}")


