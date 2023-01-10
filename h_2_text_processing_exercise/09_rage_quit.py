symbols = input().upper()
new_string = ""
last_string = ""
unique_symbols = ""
number = ""   # стринг, защото ако са две поредни числа, ще стане едно двуцифрено, a няма да ги събира

for i in range(len(symbols)):
    if not symbols[i].isdigit():
        new_string += symbols[i]
        if symbols[i] not in unique_symbols:
            unique_symbols += symbols[i]
    else:
        if i < len(symbols) - 1:            # срещу index out of range
            if symbols[i + 1].isdigit():    # проверката за две поредни числа
                number += symbols[i]
                number += symbols[i + 1]    # първото + второто като стринг прави двуцифрено число
            else:
                number += symbols[i]
        else:
            number += symbols[i]
        new_string *= int(number)
        last_string += new_string
        new_string = ""
        number = ""

print(f"Unique symbols used: {len(unique_symbols)}")
print(last_string)

