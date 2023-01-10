import re

number = int(input())
valid_password = ""
for i in range(number):
    password = input()

    pattern = r"(.+)\>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|[^\<\>]*(.{3})\<(\1)"
    matches = re.findall(pattern, password)
    if not matches:
        print("Try another password!")
    else:
        for match in matches:
            numbers = match[1]
            lower_case_letter = match[2]
            upper_case_letter = match[3]
            symbols = match[4]
            valid_password = str(numbers) + lower_case_letter + upper_case_letter + symbols
            print(f"Password: {valid_password}")

