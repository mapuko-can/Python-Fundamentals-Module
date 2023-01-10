def order(product, quantity):
    if product == "coffee":
        return 1.50 * quantity
    elif product == "water":
        return 1.00 * quantity
    elif product == "coke":
        return 1.40 * quantity
    elif product == "snacks":
        return 2.00 * quantity


current_product = input()
current_quantity = int(input())
total_price = order(current_product, current_quantity)
print(f"{total_price:.2f}")