# i=1
# while i>3: #1 2 3
#     j=1 
#     while j<4: #1  2 3 4 1 2 3 4
#         print("Welcome") 
#         j+=1
#     print(i)
#     i+=1
    

# 1
# 12
# 123
# 1234
# 12345


i=1  
while i<=5: # 1 2 3 4 5
    j=1
    while j<=i: #1 2    #1 2 3
        print(j,end="")
        j+=1 
    print()
    i+=1


#initilization
i=1
while i<3:
    #perform any task
    i+=1
    #updation