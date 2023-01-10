path = input().split("\\")
for part in path:
    if "." in part:
        file = part.split(".")
        name = file[0]
        extension = file[1]
        print(f"File name: {name}\nFile extension: {extension}")