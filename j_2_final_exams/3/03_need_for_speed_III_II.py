number_of_cars = int(input())
dictionary = {}
for i in range(number_of_cars):
    cars = input().split("|")
    current_car = cars[0]
    mileage = int(cars[1])
    current_fuel = int(cars[2])
    dictionary[current_car] = {'mileage': mileage, 'fuel': current_fuel}

commands = input()
while commands != "Stop":
    command = commands.split(" : ")
    current_command = command[0]
    car = command[1]

    if current_command == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if dictionary[car]['fuel'] < fuel:
            print("Not enough fuel to make that ride")
        else:
            dictionary[car]['mileage'] += distance
            dictionary[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if dictionary[car]['mileage'] >= 100000:
            del dictionary[car]
            print(f"Time to sell the {car}!")

    elif current_command == "Refuel":
        fuel = int(command[2])
        if fuel + dictionary[car]['fuel'] > 75:
            print(f"{car} refueled with {75 - dictionary[car]['fuel']} liters")
            dictionary[car]['fuel'] = 75
        else:
            dictionary[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif current_command == "Revert":
        kilometers = int(command[2])
        dictionary[car]['mileage'] -= kilometers
        if dictionary[car]['mileage'] < 10000:
            dictionary[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    commands = input()

for car in dictionary:
    print(f"{car} -> Mileage: {dictionary[car]['mileage']} kms, Fuel in the tank: {dictionary[car]['fuel']} lt.")