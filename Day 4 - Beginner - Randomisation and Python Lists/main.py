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

# names_string = input("Give me everybody's names.")
# names = names_string.split(",")

# # names_item = len(names)
# # random_name = random.randint(0, names_item-1)
# # bill_pay = names[random_name]
# # print(bill_pay)
# bill_pay = random.choice(names)
# print(bill_pay)

user_action = input("Enter a choice (rock, paper, scissors): ")

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both player selected {user_action}")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashed scissors! You win.")
    else:
        print("Paper covers Rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers Rock! You win.")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashed scissors! You win.")
