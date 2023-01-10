items = input().split()
searched_products = input().split()
shop = {}
for i in range(0, len(items), 2):
    key = items[i]
    value = items[i+1]
    shop[key] = int(value)
for product in searched_products:
    if product in shop:
        print(f"We have {shop[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")