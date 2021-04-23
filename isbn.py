isbn = '978-0-306-40615-7'
#isbn = '978-0-14-101111-0'
#isbn = '978-0-575-08625-8'
#isbn ='9781861972712'
short = isbn.replace('-','',-1)
total = 0

for i in range(len(short)-1):
    if i % 2 == 0:
        total += int(short[i])
    else:
        total += 3*int(short[i])

#print(int(short[-1]), 10-(total%10))
#print(type((short[-1])), type(10-(total%10)))

if int(short[-1]) == 10-(total%10):
    print("code valid")
elif int(short[-1]) == 0 and 10-(total%10) == 10:
    print("code valid")
else:
    print("Not a book, nerd")