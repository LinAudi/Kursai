print("STUDENT GRADE TRACKER: \n")

student_list = []

while True:
    number = input("Enter number of students: ")
    try:
        student_number =int(number)
        if 0 < student_number < 250:
            break
        else:
            print("The school is not registered with that many students.")
    except:
     print("Wrong input.")


def student_info(name):
    student = {}
    student_list.append(student)
    student["Name"] = name

    subject_qnty = int(input("Enter how many grades u want to enter: "))
    grades = []

    for grade in range(subject_qnty):
        while True:
            grade = int(input("Enter grade: "))
            if 0 < grade <= 100:
                grades.append(grade)
                break
            else:
                print("Wrong value.")

    student["Grades"] = grades
    return student_list

for _ in range(student_number):
    name = input("Enter student name:" )
    student_info(name)

top_average = 0
top_student = ""

for student in student_list:
    name = student["Name"]
    grades = student["Grades"]
    x = sum(grades)
    y = len(grades)
    average = round(float(x/y),2)
    print(f"Average grade of {name} is: {average}")

    if average > top_average:
        top_average = average
        top_student = name

print(f"{name.upper()} THE BEST OF THE BEST. AVERAGE  SCORE : {top_average}")