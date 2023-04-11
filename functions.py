# Functions
# starts with "def" keyword
# then it has the name of the function
# list of arguments
# the lines of code

# def greet(fname, lname):
#     print(f"Hello {fname} {lname}")

# greet("John", "Smith")
# print("let's greet another person")
# greet("Mark", "Rober")


# def is_prime(number):
#     for i in range(2, number):
#         if(number % i == 0):
#             print("Not a prime")
#             break
#     else:
#         print("A prime")

# is_prime(5)
# is_prime(6)
# is_prime(15)
# is_prime(29)


# Scope - global and local

# fname = "John"
# lname = "Smith"

# def greet():
#     fname = "Jane"
#     lname = "Doe"
#     print(fname)
#     print(lname)

# greet()

# print(fname)
# print(lname)

# Pure Functions - doesn't depend upon external variables


# return statement
# 3 + 4 - 2
def add(num1, num2):
    num3 = num1 + num2
    return num3

def subtract(num1, num2):
    return num1 - num2

sum = add(3, 4)
print(sum)
calculation = subtract(sum, 4)
print(calculation)