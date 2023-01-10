budget = float(input())
price_for_1_kg_flour = float(input())
price_for_1_pack_of_eggs = price_for_1_kg_flour * 0.75
price_for_1l_milk = price_for_1_kg_flour * 1.25
one_loaf_price = price_for_1_kg_flour + price_for_1_pack_of_eggs + (price_for_1l_milk / 4)
easter_bread_counter = 0
colored_eggs_counter = 0
while budget >= one_loaf_price:
    budget -= one_loaf_price
    easter_bread_counter += 1
    colored_eggs_counter += 3
    if easter_bread_counter % 3 == 0:
        colored_eggs_counter -= (easter_bread_counter - 2)
print(f"You made {easter_bread_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")
