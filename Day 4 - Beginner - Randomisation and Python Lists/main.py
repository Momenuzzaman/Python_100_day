import random

# random_number = random.randint(1, 10)
# print(random_number)

# random_number_float = random.random()*5
# print(random_number_float)

# love_score = random.randint(1, 100)
# print(f"You love score is {love_score}")

# exercise 1********************************

# random_number = random.randint(0, 1)

# if random_number == 1:
#     print("Head")
# else:
#     print("Tail")

names_string = input("Give me everybody's names.")
names = names_string.split(",")

# names_item = len(names)
# random_name = random.randint(0, names_item-1)
# bill_pay = names[random_name]
# print(bill_pay)
bill_pay = random.choice(names)
print(bill_pay)
