import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '$', '%', '=', ':', '?',
           '.', '/', '|', '~', '>', '*', '(', ')', '<']

print("Welcome to the Python Password generator")
nr_letter = int(
    input("How many Letters would you like in your password? :>\n"))
nr_number = int(input("How many Number would you like in your password? :>\n"))
nr_symbols = int(
    input("How many Symbols would you like in your password? :>\n"))

password_list = []

for digit in range(1, nr_letter+1):
    password_list.append(random.choice(letters))


for digit in range(1, nr_number+1):
    password_list.append(random.choice(numbers))

for digit in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))

password = ""
random.shuffle(password_list)
for char in password_list:
    password += char

print(password)
