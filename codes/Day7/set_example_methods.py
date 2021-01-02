# set_example={1,2,3}
# set_example.add(4)
# print(set_example)
# set_example.remove(4)
# print(set_example)


set_example1={1,2,3}
set_example2={1,2,3,4}
set_example3={6,7}
print(set_example1.isdisjoint(set_example2))
print(set_example1.isdisjoint(set_example3))

print(set_example2.issuperset(set_example1))
print(set_example1.issubset(set_example2))

