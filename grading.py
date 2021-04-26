def it_average(name, homework, assessment, exam):
    overall = float(((homework + assessment + exam)/175)*100)
    if overall >= 70:
        grade = 'A'
    elif overall >=60:
        grade = 'B'
    elif overall >=50:
        grade = 'C'
    elif overall >= 40:
        grade = 'D'
    else:
        grade = 'Fail'
    return(f'{name} your score was {round(overall,2)}% which is a {grade}')

# name = input("Type the students name: ")
# homework = int(input("What did they score on their homework? "))
# assessment = int(input("What did they score on their assessment? "))
# exam = int(input("What did they score on their exam? "))

name = 'Brian'
homework = 22
assessment = 38
exam = 72

print(it_average(name, homework, assessment, exam))