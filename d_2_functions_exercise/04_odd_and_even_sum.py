def odd_even_sum(numbers):
    odd_sum = 0
    even_sum = 0
    for num in numbers:
        if int(num) % 2 != 0:
            odd_sum += int(num)
        else:
            even_sum += int(num)
    return odd_sum, even_sum

string_numbers = input()
odd_sum, even_sum = odd_even_sum(string_numbers)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


