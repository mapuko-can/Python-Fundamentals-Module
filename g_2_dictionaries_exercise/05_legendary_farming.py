dictionary = {"shards": 0, "fragments": 0, "motes": 0}
input_line = input().split()
obtained = False

while not obtained:

    for i in range(0, len(input_line), 2):
        material = input_line[i + 1].lower()
        quantity = int(input_line[i])

        if material not in dictionary.keys():
            dictionary[material] = 0
        dictionary[material] += quantity

        if dictionary["shards"] >= 250:
            print("Shadowmourne obtained!")
            dictionary["shards"] -= 250
            obtained = True

        elif dictionary["fragments"] >= 250:
            print("Valanyr obtained!")
            dictionary["fragments"] -= 250
            obtained = True

        elif dictionary["motes"] >= 250:
            print("Dragonwrath obtained!")
            dictionary["motes"] -= 250
            obtained = True

        if obtained:
            break

    if obtained:
        break
    input_line = input().split()

for material, quantity in dictionary.items():
    print(f"{material}: {quantity}")

