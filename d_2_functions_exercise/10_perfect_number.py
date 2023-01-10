def perfect_number(number):
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


current_number = int(input())
perfect_number(current_number)
