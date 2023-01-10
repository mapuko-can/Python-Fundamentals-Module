command = input()
price_without_taxes = 0
taxes = 0
total_price = 0
while command != "special" and command != "regular":
    parts_price = float(command)
    if parts_price < 0:
        print("Invalid price!")
        command = input()
        continue

    price_without_taxes += parts_price
    tax = parts_price * 0.20
    taxes += tax
    price_with_taxes = parts_price + tax
    total_price += price_with_taxes

    command = input()

if command == "special":
    total_price *= 0.90

if total_price == 0:
    print("Invalid order!")

else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")

