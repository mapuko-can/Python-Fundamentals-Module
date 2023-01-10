number = int(input())
for num in range(1, number + 1):
    digits = num
    digit_sum = 0
    while digits > 0:
        digit_sum += digits % 10
        digits = digits // 10
        # digits = int(digits / 10)
    is_special = digit_sum == 5 or digit_sum == 7 or digit_sum == 11
    print(f"{num} -> {is_special}")