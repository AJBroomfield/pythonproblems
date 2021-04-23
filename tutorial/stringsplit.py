string=("biscuittins")
middle = len(string)//2

smiddle=string[middle-1:middle+2]

stringm=string[:middle-1]+ string[middle-1:middle+2].upper() +string[middle+2:]
print(stringm)