def grade_calculator(maths,chemistry,physics):
    average = round((maths + chemistry + physics)/3,2)
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

    return(f'You scored {average} which is a {grade}')   

print(grade_calculator(86,73,66))