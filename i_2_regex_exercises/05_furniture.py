import re
furnitures = []
total_price = 0
pattern = r">>([A-za-z]+)<<(\d+\.?\d*)!(\d+)"
command = input()
while command != "Purchase":
    matches = re.search(pattern, command)
    if matches:
        name, price, quantity = matches.groups()
        furnitures.append(name)
        total_price += float(price) * int(quantity)
    command = input()
print("Bought furniture:")
for furniture in furnitures:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")
