number = int(input())
dictionary = {}
for i in range(number):
    commands = input().split()
    command = commands[0]

    if command == "register":
        name = commands[1]
        license_plate_number = commands[2]
        if name not in dictionary.keys():
            dictionary[name] = license_plate_number
            print(f"{name} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif command == "unregister":
        name = commands[1]
        if name in dictionary.keys():
            del dictionary[name]
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for name, license_plate_number in dictionary.items():
    print(f"{name} => {license_plate_number}")

