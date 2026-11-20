#step:1 Take student name as input from user
student_name = input("Enter student name: ")

#step:2 Take student grades as input from user
math_marks = float(input("Enter math grade: "))
science_marks = float(input("Enter science grade: "))
english_marks = float(input("Enter english grade: "))

total_marks = math_marks + science_marks + english_marks
average_marks = total_marks / 3

# Step 3: Determine grade using if-elif-else
if average_marks >= 80:
    grade = 'A+'
elif average_marks >= 70:
    grade = 'A'
elif average_marks >= 60:
    grade = 'B'
elif average_marks >= 50:
    grade = 'C'
else:
    grade = 'F'


# Step 4: Display the result using f-strings
print("\n--- Student Result ---")
print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Grade: {grade}")
