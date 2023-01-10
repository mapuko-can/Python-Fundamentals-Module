number = int(input())
dictionary = {}
for lines in range(number):
    info = input().split("<->")
    plant = info[0]
    rarity = int(info[1])
    dictionary[plant] = {"rarity": rarity, "rating": []}

while True:
    command = input()
    if command == "Exhibition":
        break
    current_command = command.split(" ")
    current_plant = current_command[1]

    if current_plant not in dictionary:
        print("error")
        continue

    if "Rate:" in current_command:
        rating = int(current_command[-1])
        dictionary[current_plant]["rating"].append(rating)

    elif "Update:" in current_command:
        new_rarity = int(current_command[-1])
        dictionary[current_plant]["rarity"] = new_rarity

    elif "Reset:" in current_command:
        dictionary[current_plant]["rating"].clear()

print(f"Plants for the exhibition:")

for key, value in dictionary.items():
    if len(value['rating']) > 0:
        average_rating = sum(value['rating']) / len(value['rating'])
    else:
        average_rating = 0.00
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {float(average_rating):.2f}")






