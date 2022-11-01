# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm?"))

# if height >= 80:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $7")
# else:
#     print("Sorry, you have to grow taller before you can ride")






# Exercise -1********************************

# number = int(input("Which number do you want to choice?"))

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# Exercise -2****************************************************************

# height = float(input("Enter your height"))
# weight = float(input("Enter your weight"))

# bmi = weight / height ** 2
# print(bmi)

# if bmi < 18:
#     print(f"Your bmi is {bmi}, you are a underweight")
# elif bmi < 25:
#     print(f"Your bmi is {bmi}, you are a normal weight")
# elif bmi < 30:
#     print(f"Your bmi is {bmi}, you are a over weight")
# elif bmi < 35:
#     print(f"Your bmi is {bmi}, you are a obese")
# else:
#     print("clinically obese")



# Exercise -2****************************************************************

year = int(input("Which year do you want to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")