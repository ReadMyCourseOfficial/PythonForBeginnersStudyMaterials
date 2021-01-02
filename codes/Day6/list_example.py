# #creating an empty list
# list_example=[]
# print(list_example)
# #creating list
# list_example_int=[1,2,3,4]
# list_example_float=[1.0,2.0]
# list_example_string=["Welcome","Facebook","ReadMyCourse"]
# print(list_example_int)
# print(list_example_float)
# print(list_example_string)

# list_example_multi_typedata=[12,"Hello",1.0]
# print(list_example_multi_typedata)

# list_example=[1,2,3]
# print(list_example[2])
# list_example[2]=4
# print(list_example)


#assignment is done by pass by reference
# list_example1=[1,2,3,4]
# list_example2=list_example1
# list_example2[1]=9
# print(list_example1)
# print(list_example2)

#overcome 
list_example1=[1,2,3,4]
list_example2=list_example1.copy()
list_example2[1]=9
print(list_example1)
print(list_example2)


