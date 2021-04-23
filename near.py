# def near(string1, string2):

stringa = 'reset'
stringb = 'rest'


for i in range(len(stringa)):
    string1=list(stringa)
    del(string1[i])
    #print(f'{i} {string1} \n  {list(stringb)}')
    if string1==list(stringb):
        #print('TRUE')
        break
print(string1==list(stringb))


# for j in range(0):
#     for i in range(len(stringa)):
#         string1=list(stringa)
#         del(string1[i])
#         #print(f'{i} {string1} \n  {list(stringb)}')
#         if string1==list(stringb):
#             print('TRUE')
#             break
# print('FALSE')
