events = input().split("|")
total_energy = 100
total_coins = 100
is_open = True
for event in events:
    elements = event.split("-")
    event = elements[0]
    number = int(elements[1])
    if event == "rest":
        current_energy = total_energy
        total_energy += number
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += number
            print(f"You earned {number} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= number:
            total_coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            is_open = False
            break
if is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")



