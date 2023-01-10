input_line = input()
digits = []
letters = []
other_symbols = []
# digits, letters, other_symbols = [], [], []
for symbol in input_line:
    if symbol.isdigit():
        digits.append(symbol)
    elif symbol.isalpha():
        letters.append(symbol)
    else:
        other_symbols.append(symbol)
print("".join(digits))
print("".join(letters))
print("".join(other_symbols))
