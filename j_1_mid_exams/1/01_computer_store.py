command = input()
price_without_taxes = 0
taxes = 0
total_price = 0
while command != "special" and command != "regular":
    prices = float(command)
    if prices < 0:
        print("Invalid price!")
        command = input()
        continue
    price_without_taxes += prices
    taxes = 0.20 * price_without_taxes
    total_price = price_without_taxes + taxes
    command = input()
if command == "special":
    total_price = total_price - (total_price * 0.10)
if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")

# command = input()
# price_without_taxes = 0
# taxes = 0
# total_price = 0
# while command != "special" and command != "regular":
#     prices = float(command)
#     if prices < 0:
#         print("Invalid price!")
#     else:
#         price_without_taxes += prices
#         taxes = 0.20 * price_without_taxes
#         total_price = price_without_taxes + taxes
#     command = input()
# if command == "special":
#     total_price = total_price - (total_price * 0.10)
# if total_price == 0:
#     print("Invalid order!")
# else:
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {price_without_taxes:.2f}$")
#     print(f"Taxes: {taxes:.2f}$")
#     print("-----------")
#     print(f"Total price: {total_price:.2f}$")





