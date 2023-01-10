def grade(number):
    if number < 3:
        return "Fail"
    elif number < 3.50:
        return "Poor"
    elif number < 4.50:
        return "Good"
    elif number < 5.50:
        return "Very Good"
    else:
        return "Excellent"


current_number = float(input())
print(grade(current_number))
