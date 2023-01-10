water_tank_capacity = 255
number_of_lines = int(input())
total_litres = 0
for liters in range(number_of_lines):
    liters_of_water = int(input())
    total_litres += liters_of_water
    if total_litres > water_tank_capacity:
        print("Insufficient capacity!")
        total_litres -= liters_of_water
        continue
if total_litres <= water_tank_capacity:
    print(total_litres)

