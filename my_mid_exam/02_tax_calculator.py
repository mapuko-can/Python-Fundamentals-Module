vehicles = input().split(">>")
all_taxes = 0

for vehicle in vehicles:
    elements = vehicle.split()
    car_type = elements[0]
    years = int(elements[1])
    kilometers = int(elements[2])

    if car_type == "family":
        taxes = kilometers // 3000 * 12 + (50 - years * 5)
        all_taxes += taxes
        print(f"A {car_type} car will pay {taxes:.2f} euros in taxes.")

    elif car_type == "heavyDuty":
        taxes = kilometers // 9000 * 14 + (80 - years * 8)
        all_taxes += taxes
        print(f"A {car_type} car will pay {taxes:.2f} euros in taxes.")

    elif car_type == "sports":
        taxes = kilometers // 2000 * 18 + (100 - years * 9)
        all_taxes += taxes
        print(f"A {car_type} car will pay {taxes:.2f} euros in taxes.")

    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {all_taxes:.2f} euros in taxes.")
