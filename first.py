students = {
    "Rahul": 85,
    "Amit": 67,
    "Sneha": 92,
    "Priya": 45
}
total =0
highest= 0
topper ="" 

for name, marks in students.items():
    print(name, ":", marks)

    total += marks

    if marks > highest:
        highest = marks
        topper = name

    average = total / len(students)   

print(students)
print("highest marks are: ", highest, "obtained by: ", topper)
print("average of class is", average)

for name, marks in students.items():
    if marks > 75:
        print("students with marks above 75 are:", name)
