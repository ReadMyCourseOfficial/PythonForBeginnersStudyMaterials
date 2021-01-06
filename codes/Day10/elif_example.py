# if <condition1>:
#     #do something if the condition1 is true
# elif <condition2>:
#     #do something if the condition2 is true and condition1 is false
# else:
#     #do if condition1 and condition2 are false

# marks
#<80 C grade
# >80 and <90: B
# >90 and <95: A
# >95: A+

# marks=int(input("please enter the marks: "))
# if marks>95:
#     print("A+ grade")
# elif marks>90 and marks<95:
#     print("A grade")
# elif marks>80 and marks<90:
#     print("B grade")
# else:
#     print("C grade")
    
    

students={
    "Anand":78,
    "Mohit":52,
    "Shreya":99
}

student_name=input("please enter the student name")

marks=students[student_name]

if marks>95:
    print("A+ grade")
elif marks>90 and marks<95:
    print("A grade")
elif marks>80 and marks<90:
    print("B grade")
else:
    print("C grade")

if 
