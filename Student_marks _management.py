# Create a dictionary containing student names and their marks.

# Example:
# students = {    "Rahul": 85,    "Amit": 67,    "Sneha": 92,    "Priya": 45}



# Write a program to:
# 1. Display all students and their marks.
# 2. Find the student with the highest marks.
# 3. Calculate the class average.
# 4. Display students who scored above 75.

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
