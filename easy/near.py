def near(string1, string2):

    fixed_string1 = string1
    fixed_string2 = string2


    for i in range(len(fixed_string1)):
        string1=list(fixed_string1)
        del(string1[i])
        if string1==list(fixed_string2):
            break
    return(string1==list(fixed_string2))


print(near('reset','rest'))
print(near('dragoon','dragon'))
print(near('eave','leave'))
print(near('sleets','lets'))