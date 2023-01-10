number = int(input())
dictionary = {}
for i in range(number):
    heroes = input().split()
    hero = heroes[0]
    hit_points = int(heroes[1])
    mana_points = int(heroes[2])
    dictionary[hero] = {'HP': hit_points, 'MP': mana_points}

command = input()
while command != "End":
    commands = command.split(" - ")
    current_command = commands[0]
    hero_name = commands[1]

    if current_command == "CastSpell":
        mp_needed = int(commands[2])
        spell_name = commands[3]
        if dictionary[hero_name]['MP'] >= mp_needed:
            dictionary[hero_name]['MP'] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {dictionary[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif current_command == "TakeDamage":
        damage = int(commands[2])
        attacker = commands[3]
        dictionary[hero_name]['HP'] -= damage
        if dictionary[hero_name]['HP'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {dictionary[hero_name]['HP']} HP left!")
        else:
            del dictionary[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif current_command == "Recharge":
        amount = int(commands[2])
        if dictionary[hero_name]['MP'] + amount > 200:
            print(f"{hero_name} recharged for {200 - dictionary[hero_name]['MP']} MP!")
            dictionary[hero_name]['MP'] = 200
        else:
            dictionary[hero_name]['MP'] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif current_command == "Heal":
        amount = int(commands[2])
        if dictionary[hero_name]['HP'] + amount > 100:
            print(f"{hero_name} healed for {100 - dictionary[hero_name]['HP']} HP!")
            dictionary[hero_name]['HP'] = 100
        else:
            dictionary[hero_name]['HP'] += amount
            print(f"{hero_name} healed for {amount} HP!")
    command = input()

for hero in dictionary:
    print(f"{hero}\n  HP: {dictionary[hero]['HP']}\n  MP: {dictionary[hero]['MP']}")


