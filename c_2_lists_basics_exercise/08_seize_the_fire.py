fires = input().split('#')
amount_of_water = int(input())
total_effort = 0
total_fire = 0
put_out_cells = []
for fire in fires:
    elements = fire.split(" = ")
    fire_type = elements[0]
    value = int(elements[1])
    is_valid = False
    if amount_of_water < value:
        continue
    if fire_type == 'High':
        if 81 <= value <= 125:
            is_valid = True
    elif fire_type == 'Medium':
        if 51 <= value <= 80:
            is_valid = True
    elif fire_type == 'Low':
        if 1 <= value <= 50:
            is_valid = True
    if is_valid:
        put_out_cells.append(value)
        total_effort += value * 0.25
        total_fire += value
        amount_of_water -= value
print("Cells:")
for cell in put_out_cells:
    print(f' - {cell}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')


