students={
    "Anand":45,
    "Pankaj":43,
    "Virat":80
}

#add a new student in the database
# student_name=input("please enter the student name")
# student_marks=float(input("please enter the student marks"))

# students.update({student_name:student_marks})
# print(students)

#to get the summ of all the scores
sum_of_score=sum(students.values())
print("the sum of all the students marks is",sum_of_score)

#to get the average score of the students
average_score=sum(students.values())/len(students)
print("avergae score of the students is",average_score)