# list_example=[1,2,3,4,5,6,7,7,8,8]

# set_example={1,2,3,4,1}
# set_example1=set(list_example)
# print(set_example1)
# list_example=list(set_example1)
# print(list_example)


set_example1={1,2,3,4,5}
set_example2={4,5,6,7}
#union
# result=set_example1|set_example2
# print(result)

# #intersaction
# result=set_example1&set_example2
# print(result)

# #difference
# result=set_example1-set_example2
# print(result)

# #symmetric difference
# result=set_example1^set_example2
# print(result)

set_example1={1,2,3,4,5}
set_example2={4,5,6,7}
#union
# result=set_example1|set_example2
# print(result)
# result=set_example1.union(set_example2)
# print(result)
# #intersaction
# #result=set_example1&set_example2
# result=set_example1.intersection(set_example2)
# print(result)

# #difference
# #result=set_example1-set_example2
# result=set_example1.difference(set_example2)
# print(result)

# #symmetric intersaction
# result=set_example1^set_example2
# result=set_example1.symmetric_difference(set_example2)
# print(result)

#intersaction

set_example1={1,2,3,4,5}
set_example2={4,5,6,7}

# set_example1.intersection_update(set_example2)
set_example1.difference_update(set_example2)

#print(set_example1)
print(set_example2)

