command = input()
dictionary = {}

while command != "Sail":
    targets = command.split("||")
    city, population, gold = targets[0], int (targets[1]), int(targets[2])
    if city not in dictionary:
        dictionary[city] = {"population": population, "gold": gold}
    else:
        dictionary[city]["population"] += population
        dictionary[city]["gold"] += gold
    command = input()

input_lines = input()
while input_lines != "End":
    events = input_lines.split("=>")
    current_command = events[0]
    town = events[1]

    if current_command == "Plunder":
        people = int(events[2])
        gold = int(events[3])
        dictionary[town]['population'] -= people
        dictionary[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if dictionary[town]['population'] <= 0 or dictionary[town]['gold'] <= 0:
            del dictionary[town]
            print(f"{town} has been wiped off the map!")

    elif current_command == "Prosper":
        gold = int(events[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            dictionary[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {dictionary[town]['gold']} gold.")
    input_lines = input()

if len(dictionary) > 0:
    print(f"Ahoy, Captain! There are {len(dictionary)} wealthy settlements to go to:")
    for town in dictionary:
        print(f"{town} -> Population: {dictionary[town]['population']} citizens, Gold: {dictionary[town]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")