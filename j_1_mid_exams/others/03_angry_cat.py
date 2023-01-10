price_rating = input().split(", ")
entry_point = int(input())
command = input()
left_sum = 0
right_sum = 0
entry_number = int(price_rating[entry_point])

for index, item in enumerate(price_rating):
    item = int(item)

    if command == "cheap":
        if index < entry_point and item < entry_number:
            left_sum += item
        elif index > entry_point and item < entry_number:
            right_sum += item

    elif command == "expensive":
        if index < entry_point and item >= entry_number:
            left_sum += item
        elif index > entry_point and item >= entry_number:
            right_sum += item

if left_sum > right_sum:
    print(f"Left - {left_sum}")
elif right_sum > left_sum:
    print(f"Right - {right_sum}")
else:
    print(f"Left - {left_sum}")



