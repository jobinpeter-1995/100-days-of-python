# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#print(student_heights)

sum = 0
final = 0
count = 0

for test in student_heights:
    sum = test
    final = sum + final
    count += 1

avg = round(final / count) 

print(f"{avg}")
