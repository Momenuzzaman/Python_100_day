# fruits = ["Apple", "Banana", "Maroon", "Orange"]
# for fruit in fruits:
#     print(fruit)

# student_heights = input("Input a list of student height :").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# 1st logic
# total_height = 0
# for height in student_heights:
#     total_height += height

# student_len = 0
# for student in student_heights:
#     student_len += 1

# avg = round(total_height / student_len)
# print(avg)


# 2nd logic
# student_height_sum = (sum(student_heights))
# student_len = len(student_heights)
# avg = round(student_height_sum / student_len)
# print(avg)


# exercise 2************************************************

# student_score = input("Input a list of student scores :").split()
# for n in range(0, len(student_score)):
#     student_score[n] = int(student_score[n])

# max_score = 0
# for score in student_score:
#     if score > max_score:
#         max_score = score


# # max_score= max(student_score)
# print(f"The highest score in the class is: {max_score}")


# min_score = min(student_score)
# print(f"The lowest score in the class is: {min_score}")

# last_number = input("Enter last number :")
# last_number = int(last_number)+1
# total = 0
# for i in range(1, last_number):
#     total += i
# print(total)

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
