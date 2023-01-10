number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0
for snowball in range(number_of_snowballs):
    weight_of_the_snowball = int(input())
    time_to_get_target = int(input())
    quality_of_the_snowball = int(input())
    value = (weight_of_the_snowball / time_to_get_target) ** quality_of_the_snowball
    if value > max_value:
        max_value = value
        max_weight = weight_of_the_snowball
        max_time = time_to_get_target
        max_quality = quality_of_the_snowball
print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")