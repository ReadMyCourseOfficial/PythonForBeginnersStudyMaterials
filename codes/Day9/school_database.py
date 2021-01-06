#application of list
students=["Anand","Pankaj","Manoj"]
# student_to_check=input("please enter the student name to check:")
# is_student_present=student_to_check in students
# print(is_student_present)
# stundent_to_store=input("please enter the student name")
# students.append(stundent_to_store)
# print(students)

#to get only unique students in the database

students=["Anand","Pankaj","Manoj","Manoj"]
print("Our school database is ",students)
unique_students=set(students)
print("Unique students present in the databse is: ",unique_students)
