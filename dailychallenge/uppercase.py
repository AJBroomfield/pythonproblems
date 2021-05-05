def upper_letters(word):
    solution=[]
    word=list(word)
    for i in range(len(word)):
        if word[i].isupper() == True:
            solution.append((word[i],i))
    return solution

print(upper_letters('HeLLo World!'))

