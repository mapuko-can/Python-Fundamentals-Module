number_of_orders = int(input())
total_price = 0
for orders in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    price = price_per_capsule * capsules * days
    if 0.01 > price_per_capsule or price_per_capsule > 100.00:
        continue
    if 1 > days or days > 31:
        continue
    if 1 > capsules or capsules > 2000:
        continue
    else:
        print(f"The price for the coffee is: ${price:.2f}")
    total_price += price
print(f"Total: ${total_price:.2f}")
