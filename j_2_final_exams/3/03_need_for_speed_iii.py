# number = int(input())
# dictionary = {}
# for line in range(number):
#     cars = input().split("|")
#     car = cars[0]
#     mileage = int(cars[1])
#     fuel = int(cars[2])
#     dictionary[car] = {"mileage": mileage, "fuel": fuel}
#
# command = input()
# while command != "Stop":
#     commands = command.split(" : ")
#     current_command = commands[0]
#     current_car = commands[1]
#
#     if current_command == "Drive":
#         distance = int(commands[2])
#         current_fuel = int(commands[3])
#         if dictionary[current_car]["fuel"] < current_fuel:
#             print("Not enough fuel to make that ride")
#         else:
#             dictionary[current_car]["mileage"] += distance
#             dictionary[current_car]["fuel"] -= current_fuel
#             print(f"{current_car} driven for {distance} kilometers. {current_fuel} liters of fuel consumed.")
#         if dictionary[current_car]["mileage"] >= 100000:
#             del dictionary[current_car]
#             print(f"Time to sell the {current_car}!")
#
#     elif current_command == "Refuel":
#         current_fuel = int(commands[2])
#         fuel = dictionary[current_car]["fuel"]
#         if current_fuel + fuel > 75:
#             print(f"{current_car} refueled with {75 - fuel} liters")
#             dictionary[current_car]["fuel"] = 75
#         else:
#             dictionary[current_car]["fuel"] += current_fuel
#             print(f"{current_car} refueled with {current_fuel} liters")
#
#     elif current_command == "Revert":
#         kilometers = int(commands[2])
#         dictionary[current_car]["mileage"] -= kilometers
#         if dictionary[current_car]["mileage"] < 10000:
#             dictionary[current_car]["mileage"] = 10000
#         else:
#             print(f"{current_car} mileage decreased by {kilometers} kilometers")
#     command = input()
#
# for car in dictionary:
#     print(f'{car} -> Mileage: {dictionary[car]["mileage"]} kms, Fuel in the tank: {dictionary[car]["fuel"]} lt.')

number = int(input())
dictionary = {}
for line in range(number):
    cars = input().split("|")
    car = cars[0]
    mileage = int(cars[1])
    fuel = int(cars[2])
    dictionary[car] = {"mileage": mileage, "fuel": fuel}


def drive(car, distance, fuel):
    if dictionary[car]["fuel"] < fuel:
        print("Not enough fuel to make that ride")
    else:
        dictionary[car]["mileage"] += distance
        dictionary[car]["fuel"] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    if dictionary[car]["mileage"] >= 100000:
        del dictionary[car]
        print(f"Time to sell the {car}!")


def refuel(car, fuel):
    current_fuel = dictionary[car]["fuel"]
    if current_fuel + fuel > 75:
        print(f"{car} refueled with {75 - current_fuel} liters")
        dictionary[car]["fuel"] = 75
    else:
        dictionary[car]["fuel"] += fuel
        print(f"{car} refueled with {fuel} liters")


def revert(car, kilometers):
    dictionary[car]["mileage"] -= kilometers
    if dictionary[car]["mileage"] < 10000:
        dictionary[car]["mileage"] = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")


command = input()
while command != "Stop":
    commands = command.split(" : ")
    current_command = commands[0]
    current_car = commands[1]

    if current_command == "Drive":
        current_distance = int(commands[2])
        current_fuel = int(commands[3])
        drive(current_car, current_distance, current_fuel)

    elif current_command == "Refuel":
        current_fuel = int(commands[2])
        refuel(current_car, current_fuel)

    elif current_command == "Revert":
        current_kilometers = int(commands[2])
        revert(current_car, current_kilometers)
    command = input()

for car in dictionary:
    print(f'{car} -> Mileage: {dictionary[car]["mileage"]} kms, Fuel in the tank: {dictionary[car]["fuel"]} lt.')




