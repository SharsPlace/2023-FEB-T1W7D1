# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.


# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples(lower_limit = 0, higher_limit = 1000, multiple1 = 3, multiple2 = 5):
    sum = 0
    # Iterate from 0 to 1000
    for n in range(lower_limit, higher_limit):
        # add it to sum if multiple of 3 or 5
        if n % multiple1 == 0 or n % multiple2 == 0:
            sum += n


    # print the sum
    return sum

print(sum_of_multiples(multiple1 = 3, multiple2 = 5))