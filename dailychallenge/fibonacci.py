def f(n):
    solution = ""
    sequence = [0, 1]
    if type(n)==float or type(n)==str or type(n)==complex or n < 0:
        solution += "Not a valid data type"
        return solution
    else:
        if n <=1:
            return(sequence[n])    
        else:
            for x in range(2,n+1):
                next = int(sequence[x-1]) + int(sequence[x-2])
                sequence.append(next)

            return sequence[n]