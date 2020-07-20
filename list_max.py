# Author: Erika Tharp
# Date: 07/19/2020
# Description: This program contains a function called list_max which takes a list of numbers as a parameter and returns the maximum number in that
#              list using. This function is a recursive function.


def list_max(numbers):
    """
    This is a recursive function takes a list of numbers as a parameter and returns the maximum number in that list.
    """
    if len(numbers) == 1:
        return numbers[0]
    if numbers[0] > list_max(numbers[1:]):
        return numbers[0]
    else:
        return list_max(numbers[1:])

