number_of_heroes = int(input())
dictionary = {}
for lines in range(number_of_heroes):
    input_line = input().split()
    name = input_line[0]
    hit_points = int(input_line[1])
    mana_points = int(input_line[2])
    dictionary[name] = {"HP": hit_points, "MP": mana_points}
    
commands = input()
while commands != "End":
    command = commands.split(" - ")
    current_command = command[0]
    hero_name = command[1]

    if current_command == "CastSpell":
        mana_points_needed = int(command[2])
        spell_name = command[3]
        if dictionary[hero_name]["MP"] >= mana_points_needed:
            dictionary[hero_name]["MP"] -= mana_points_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {dictionary[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif current_command == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        dictionary[hero_name]["HP"] -= damage
        if dictionary[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {dictionary[hero_name]['HP']} HP left!")
        else:
            del dictionary[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif current_command == "Recharge":
        amount = int(command[2])
        if dictionary[hero_name]["MP"] + amount < 200:
            dictionary[hero_name]["MP"] += amount
            print(f"{hero_name} recharged for {amount} MP!")
        elif dictionary[hero_name]["MP"] + amount == 200:
            dictionary[hero_name]['MP'] = 200
            print(f"{hero_name} recharged for {amount} MP!")
        else:
            print(f"{hero_name} recharged for {200 - dictionary[hero_name]['MP']} MP!")
            dictionary[hero_name]['MP'] = 200

    elif current_command == "Heal":
        amount = int(command[2])
        if dictionary[hero_name]["HP"] + amount < 100:
            dictionary[hero_name]["HP"] += amount
            print(f"{hero_name} healed for {amount} HP!")
        elif dictionary[hero_name]["HP"] + amount == 100:
            dictionary[hero_name]['HP'] = 100
            print(f"{hero_name} healed for {amount} HP!")
        else:
            print(f"{hero_name} healed for {100 - dictionary[hero_name]['HP']} HP!")
            dictionary[hero_name]['HP'] = 100
    commands = input()

for hero in dictionary:
    print(f'{hero}\n  HP: {dictionary[hero]["HP"]}\n  MP: {dictionary[hero]["MP"]}')





