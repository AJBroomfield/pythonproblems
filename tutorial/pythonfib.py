my_list=[1,1,2,3,5,8,13,21,34,55,89]
solution = list()
for i in range(len(my_list)):
    if my_list[i] < 5:
        solution.append(my_list[i])
    else:
        continue
#print(solution)    

usr=int(input("Give me a number: "))
print([x for x in my_list if x<usr])

