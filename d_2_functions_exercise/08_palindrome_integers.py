def palindrome(string):
    for number in string:
        if number == number[::-1]:
            print(True)
        else:
            print(False)


numbers = input().split(', ')
palindrome(numbers)





