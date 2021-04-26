def even_digits(start, finish):
    
    solution = []
    
    for value in range(start, finish+1):
        number = str(value)
        remainder = 0
        for digit in number:
            remainder += int(digit)%2
        if remainder == 0:
            solution += [number]
    str_solution=", ".join(solution)
    
    return(str_solution)

