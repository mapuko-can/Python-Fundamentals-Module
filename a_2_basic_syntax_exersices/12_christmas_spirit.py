quantity_of_decorations = int(input())
days = int(input())
price_ornament_set = 2
price_tree_skirt = 5
price_tree_garland = 3
price_tree_lights = 15
budget = 0
total_points = 0
for day in range(1, days + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        budget += quantity_of_decorations * price_ornament_set
        total_points += 5
    if day % 3 == 0:
        budget += quantity_of_decorations * (price_tree_skirt + price_tree_garland)
        total_points += 13
    if day % 5 == 0:
        budget += quantity_of_decorations * price_tree_lights
        total_points += 17
        if day % 3 == 0:
            total_points += 30
    if day % 10 == 0:
        total_points -= 20
        budget += price_tree_skirt + price_tree_garland + price_tree_lights
if days % 10 == 0:
    total_points -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {total_points}")



