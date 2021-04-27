def timetable(size):
    
    solution = ''
    for x in range(1, size+1): 
        for y in range(1, size+1):
            solution += str(x*y) + (' '*(9-len(str(x*y))))
        
        solution += '\n'
    return solution

print(timetable(10))


