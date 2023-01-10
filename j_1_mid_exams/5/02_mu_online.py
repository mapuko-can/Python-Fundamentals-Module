rooms = input().split("|")
health = 100
bitcoins = 0
best_room = 0
# is_dead = False
for i in range(len(rooms)):
    best_room += 1
    command = rooms[i].split()

    if command[0] == "potion":
        amount = int(command[1])
        if health + amount > 100:
            amount = 100 - health
            health = 100
        else:
            health += amount
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")

    elif command[0] == "chest":
        print(f"You found {int(command[1])} bitcoins.")
        bitcoins += int(command[1])

    else:
        health -= int(command[1])
        if health > 0:
            print(f"You slayed {command[0]}.")
        else:
            print(f"You died! Killed by {command[0]}.")
            print(f"Best room: {best_room}")
            # is_dead = True
            break

# if not is_dead:
if health > 0:
    print("You've made it!")

    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
