# items = input().split("|")
# budget = float(input())
# sells = 0
# new_budget = 0
# profit = 0
# bought_items = []
# for item in items:
#     elements = item.split("->")
#     item_type = elements[0]
#     price = float(elements[1])
#     if budget >= price:
#         if item_type == "Clothes":
#             if price > 50.00:
#                 continue
#             else:
#                 budget -= price
#                 clothes_sell = price * 1.40
#                 profit += clothes_sell - price
#                 sells += clothes_sell
#                 bought_items.append(clothes_sell)
#         elif item_type == "Shoes":
#             if price > 35.00:
#                 continue
#             else:
#                 budget -= price
#                 shoes_sell = price * 1.40
#                 profit += shoes_sell - price
#                 sells += shoes_sell
#                 bought_items.append(shoes_sell)
#         elif item_type == "Accessories":
#             if price > 20.50:
#                 continue
#             else:
#                 budget -= price
#                 accessories_sell = price * 1.40
#                 profit += accessories_sell - price
#                 sells += accessories_sell
#                 bought_items.append(accessories_sell)
# new_budget = budget + sells
# for item in bought_items:
#     print(f'{item:.2f}', end=' ')
# print()
# print(f"Profit: {profit:.2f}")
# if new_budget >= 150:
#     print("Hello, France!")
# else:
#     print('Not enough money.')



