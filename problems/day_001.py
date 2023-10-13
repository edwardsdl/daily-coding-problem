# Good morning! Here's your coding interview problem for today.
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list
# add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?


def run(numbers: list[int], k: int) -> bool:
    numbers_seen: dict[int, bool] = {}
    for number in numbers:
        difference = k - number
        if difference in numbers_seen:
            return True

        numbers_seen[number] = True

    return False
