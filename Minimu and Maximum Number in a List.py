# Write a function that returns both the minimum and maximum number of the given list/array.

def min_max(lst):
    minimum = lst[0]
    maximum = lst[0]

    for number in lst:
        if number < minimum:
            minimum = number
        elif number > maximum:
            maximum = number
        else:
            pass
    return [minimum, maximum]