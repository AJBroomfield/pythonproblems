size = 5

# for x in range(1, size+1): 
#     print([(x*y) for y in range(1, size+1)])

# x = ([i for i in range(1, 6)])
# print(x)

solution = [[(x*y) for x in range(1, size+1)] for y in range(1, size+1)]

print(solution, end=',')