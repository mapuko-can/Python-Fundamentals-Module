treasure_chest = list(input().split("|"))
sum_items = 0
command = input()

while command != "Yohoho!":
    commands = command.split()
    command_one = commands[0]

    if command_one == "Loot":
        for i in range(len(commands)):
            if i == 0:
                continue
            if commands[i] not in treasure_chest:
                treasure_chest.insert(0, commands[i])

    elif command_one == "Drop":
        index = int(commands[1])
        if index in range(len(treasure_chest)):
            current_loot = treasure_chest[index]
            treasure_chest.remove(current_loot)
            treasure_chest.append(current_loot)

    elif command_one == "Steal":
        count = int(commands[1])
        if count >= len(treasure_chest):
            removed = treasure_chest
            print(", ".join(removed))
            print("Failed treasure hunt.")
            exit()
        else:
            removed = treasure_chest[-count:]
            del treasure_chest[-count:]
            print(', '.join(removed))
    command = input()
if len(treasure_chest) > 0:
    for i in range(len(treasure_chest)):
        sum_items += len(treasure_chest[i])
        average = sum_items / len(treasure_chest)
        print(f"Average treasure gain: {average:.2f} pirate credits.")