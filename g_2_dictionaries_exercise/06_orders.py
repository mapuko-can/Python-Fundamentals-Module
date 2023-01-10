products = {}
command = input()
while command != "buy":
    product, price, quantity = command.split()
    if product not in products:
        products[product] = [float(price), int(quantity)]
    else:
        products[product][0] = float(price)
        products[product][1] += int(quantity)
    command = input()
for product in products.keys():
    total_price = products[product][0] * products[product][1]
    print(f"{product} -> {total_price:.2f}")