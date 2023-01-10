dictionary = {}

while True:
    command = input().split("||")
    if command[0] == "Sail":
        break
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city not in dictionary:
        dictionary[city] = {"population": population, "gold": gold}
    else:
        dictionary[city]["population"] += population
        dictionary[city]["gold"] += gold

events = input()
while events != "End":
    commands = events.split("=>")
    event = commands[0]
    town = commands[1]
    if event == "Plunder":
        people = int(commands[2])
        gold = int(commands[3])
        dictionary[town]["gold"] -= gold
        dictionary[town]["population"] -= people
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if dictionary[town]["gold"] == 0 or dictionary[town]["population"] == 0:
            del dictionary[town]
            print(f"{town} has been wiped off the map!")
    elif event == "Prosper":
        gold = int(commands[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            dictionary[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {dictionary[town]['gold']} gold.")
    events = input()

if len(dictionary) <= 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(dictionary)} wealthy settlements to go to:")
for town in dictionary:
    print(f"{town} -> Population: {dictionary[town]['population']} citizens, Gold: {dictionary[town]['gold']} kg")





