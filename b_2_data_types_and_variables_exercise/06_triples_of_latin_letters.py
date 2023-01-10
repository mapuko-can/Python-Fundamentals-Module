number_of_letters = int(input())
for letter_one in range(number_of_letters):
    for letter_two in range(number_of_letters):
        for letter_three in range(number_of_letters):
            print(f"{chr(97 + letter_one)}{chr(97 + letter_two)}{chr(97 + letter_three)}")