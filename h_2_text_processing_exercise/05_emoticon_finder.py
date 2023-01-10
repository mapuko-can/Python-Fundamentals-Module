single_string = input()
for i in range(len(single_string)):
    if single_string[i] == ":":
        print(f":{single_string[i+1]}")