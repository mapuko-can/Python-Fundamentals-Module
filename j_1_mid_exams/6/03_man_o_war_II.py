pirate_ship = [int(number) for number in input().split('>')]
warship = [int(number) for number in input().split('>')]
max_health = int(input())
commands = input()

while commands != "Retire":
    commands = commands.split()
    command = commands[0]

    if command == "Fire":
        index = int(commands[1])
        damage = int(commands[2])
        if index in range(len(warship)):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()

    elif command == "Defend":
        index = int(commands[1])
        end_index = int(commands[2])
        damage = int(commands[3])
        if index in range(len(pirate_ship)) and end_index in range(len(pirate_ship)):
            for section in range(index, end_index + 1):
                pirate_ship[section] -= damage
                if pirate_ship[section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif command == "Repair":
        index = int(commands[1])
        health = int(commands[2])
        if index in range(len(pirate_ship)):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health

    elif command == "Status":
        count_section = 0
        for section in pirate_ship:
            if section < max_health * 0.20:
                count_section += 1
        print(f"{count_section} sections need repair.")

    commands = input()

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")