# if <condition>:
#     #body
# else:
#     body


# a=8
# if a%2==0:
#     print("Number is even")
# else:
#     print("Number is odd")


# a=int(input("please enter the number: "))
# if a%2==0:
#     print("you have entered an even number")
# else:
#     print("you have entered an odd number")
    
list_students=["Anand","Rishi","Shreya"]

student_input=input("please enter the stuedent name")
if student_input in list_students:
    print("student is present in the list")
    print("student is present at the index",list_students.index(student_input))
else:
    print("student is not present in the list")
