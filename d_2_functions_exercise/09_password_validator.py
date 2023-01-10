def validator(password):
    digit_count = 0
    for element in password:
        if element.isdigit():
            digit_count += 1
    if digit_count < 2:
        print("Password must have at least 2 digits")
    elif len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
    elif not password.isalnum():
        print("Password must consist only of letters and digits")

    else:
        print("Password is valid")


current_password = input()
validator(current_password)
