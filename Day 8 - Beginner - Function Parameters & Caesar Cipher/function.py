import math
# def greet():
#     print('Emon')
#     print('Liton')
#     print('Ruhi')


# greet()

# def my_function(name):
#     print(f'How are you {name}?')

# my_function('Emon')
# my_function('Liton')

# def greet_with(name, location):
#     print(f'Hello {name}')
#     print(f'What is it like in {location}?')


# greet_with('Emon', 'bangladesh')

# def paint_calc(height, width, cover):
#     area = height * width
#     number_of_can = math.ceil(area / cover)
#     print(f"You'all need {number_of_can} can of print")


# test_h = int(input("Height of wall:"))
# test_w = int(input("Width of wall:"))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's prime number")
    else:
        print("It's not prime number")


n = int(input("Check this number:"))
prime_checker(number=n)
