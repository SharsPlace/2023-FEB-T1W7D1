# print numbers from 1 to 5

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# while loop
# number = 1
# while number <= 5: # 1 <= 5? yes // 2 <= 5? yes ... 6 <= 5? no
#     print(number) # 1 2 ... 5
#     number += 1 # number = number + 1

# print("The end")


# login_attempts = 5
# actual_password = "hello"

# while login_attempts > 0:
#     password = input("Enter password: ")
#     if(password != actual_password):
#         print("Password Wrong!!")
#         login_attempts -= 1
#         print(f"Remaining attempts: {login_attempts}")
#     else:
#         print("Login Successful")
#         break

# print("The end")


# For loop

# students = [ "John", "Jane", "Mike" ]

# for student in students:
#     print(student)

# List all numbers between 10 and 100, and state whether they are odd or even
# for i in range(10, 100):
#     if(i % 2 == 0):
#         print(f"number {i} is even")
#     else:
#         print(f"number {i} is odd")


# for...else
# for i in range(10):
#     print(i)
#     if( i == 7 ):
#         break
# else:
#     print("Loop finished inside")

# print("Loop finished outside")


# determine if a number is a prime
# number = 6
# for i in range(2, number):
#     if(number % i == 0):
#         print("Not a prime")
#         break
# else:
#     print("A prime")