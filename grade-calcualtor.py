maths=int(input("Please enter your maths mark: "))
chemistry=int(input("Please enter your chemistry mark: "))
physics=int(input("Please enter your physics mark: "))

average = round((maths + chemistry + physics)/3,2)

print(f'Your percentage score is {average}%')


if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "You failed"

print(f'You scored a grade of: {grade}')   