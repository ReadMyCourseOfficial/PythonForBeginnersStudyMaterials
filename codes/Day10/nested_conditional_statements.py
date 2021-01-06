students={
    "Anand":78,
    "Mohit":52,
    "Shreya":99
}

student_input=input("please enter the student name: ")

if student_input in students.keys():
    marks=students[student_input]
    if marks>90:
        print("A grade")
    else:
        print("B grade")
else:
    print("student is not present in the dictionary")