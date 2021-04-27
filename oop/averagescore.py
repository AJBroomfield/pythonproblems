class Student:
    def __init__(self, name, age, cl):
        self.name = name
        self.age = age
        self.cl= "student"

    def scores(self, english, maths, science):
        return f'{round(((english+maths+science)/3),2)}%'

clive = Student("Clive", "16", "Student")
luke = Student("Luke", "15", "Student")

print(Student.scores(clive, 44,56,67))
print(Student.scores(luke, 55,66,77))