# fruits = ["Apple", "Banana", "Maroon", "Orange"]
# for fruit in fruits:
#     print(fruit)

student_heights = input("Input a list of student height :").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

student_len = 0
for student in student_heights:
    student_len += 1

avg = round(total_height / student_len)
print(avg)

# student_height_sum = (sum(student_heights))
# student_len = len(student_heights)
# avg = round(student_height_sum / student_len)
# print(avg)
