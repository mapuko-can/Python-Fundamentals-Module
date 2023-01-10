houses = list(map(int, input().split("@")))
commands = input()
position = 0
current_index = 0
house_count = 0
while commands != "Love!":
    commands = commands.split()
    jump_length = int(commands[1])
    position += jump_length
    if position not in range(len(houses)):
        position = 0
    if houses[position] != 0:
        houses[position] -= 2
        if houses[position] == 0:
            house_count += 1
            print(f"Place {position} has Valentine's day." )
    else:
        print(f"Place {position} already had Valentine's day.")
    commands = input()
print(f"Cupid's last position was {position}.")
if house_count == len(houses):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(houses) - house_count} places.")