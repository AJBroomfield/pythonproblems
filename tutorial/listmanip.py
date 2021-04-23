my_list = [5, 10, 15, 20, -25, -30]
my_list2 = ['a','b','c','d','e','f']


list1 = [my_list[0],my_list[-1]]
print(list1)

list2=[]
for i in my_list:
    list2.extend([i,i])
#print(list2)


list3=list(reversed(my_list))
print(list3)

my_list.sort()
my_list.reverse()
print(my_list)