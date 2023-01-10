command = input()
while command != "End":
    string = command
    if string != "SoftUni":
        for letter in string:
            string = letter + letter
            print(f"{string}", end="")
        print()
    command = input()

# current_string = input()
# while current_string != "End":
#     if current_string == "SoftUni":
#         current_string = input()
#         continue
#     for index, digit in enumerate(current_string):
#         print(2 * digit, end="")
#     print()
#     current_string = input()



