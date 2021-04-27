def isbncheck(code):
    short = code.replace('-','',-1)
    total = 0
    check = 0
    for i in range(len(short)-1):
        if i % 2 == 0:
            total += int(short[i])
        else:
            total += 3*int(short[i])

    if int(short[-1]) == 10-(total%10):
        check = 'Code valid!'
        
    elif int(short[-1]) == 0 and 10-(total%10) == 10:
        check = 'Code valid!'
        
    else:
        check = 'Not a book nerd'
        
    print(check)


isbncheck('978030640615-7')
isbncheck('978-0-14-101111-0')
isbncheck('978-0-575-08625-8')
isbncheck('978186197274712')