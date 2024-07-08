name = input("Your name: ")
subjects = ["Maths", "Science", "Social", "Nepali"]
total_marks = 100  # Assuming total marks are 100 per subject

student_info = {}
student_info["name"] = name
student_info["subjects"] = {}
total_obtained = 0

for subject in subjects:
    while True:
        try:
            marks = int(input(f"Enter your marks obtained in {subject} ({total_marks} marks): "))
            if 0 <= marks <= total_marks:
                break
            else:
                print("Invalid marks. Please enter a value between 0 and", total_marks)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    student_info["subjects"][subject] = marks
    total_obtained += marks

student_info["total_marks"] = total_obtained
student_info["percentage"] = (total_obtained / (len(subjects) * total_marks)) * 100

# Determine letter grade using conditional statements
if student_info["percentage"] >= 90:
    student_info["letter_grade"] = "A"
elif student_info["percentage"] >= 80:
    student_info["letter_grade"] = "A-"
elif student_info["percentage"] >= 70:
    student_info["letter_grade"] = "B"
elif student_info["percentage"] >= 60:
    student_info["letter_grade"] = "B-"
elif student_info["percentage"] >= 50:
    student_info["letter_grade"] = "c"
else:
    student_info["letter_grade"] = "Fail"

# Print results
print("\n*** Student Grade Report ***")
print(f"Student Name: {student_info['name']}")
for subject, marks in student_info["subjects"].items():
    print(f"{subject}: {marks} marks out of {student_info['total_marks']}")
print(f"Total Marks: {student_info['total_marks']}")
print(f"Percentage: {student_info['percentage']:.2f}%")
print(f"Letter Grade: {student_info['letter_grade']}")

    





    
 
 