print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? :"))
bill = 0
if height >= 80:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? :"))
    if age < 12:
        bill = 5
        print("Child ticket are $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket are $7")
    else:
        bill = 12
        print("Adult ticket are $12")
    want_photo = input("Do you want a photo taken? Y or N :")
    if want_photo == "Y":
        bill = bill + 3
        print(f"Your final bill is ${bill}")
    else:
        bill
        print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")






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



# Exercise -3****************************************************************

# year = int(input("Which year do you want to check?"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")