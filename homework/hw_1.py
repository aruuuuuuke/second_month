class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'My full name is {self.full_name},\nI am {self.age} years old.')
        if self.is_married:
            print("I am married")
        else:
            print("I'm not married")


class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def Average(self):
        for subject in self.marks:
            average = sum(self.marks[subject]) / len(self.marks[subject])
            print(f"Average mark for {subject}: {average}")


class Teacher(Person):
    base_salary = 30000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def introduce_myself(self):
        super().introduce_myself()
        print(f'I have {self.experience} years of experience.')

    def Salary(self):
        bonus = self.base_salary / 100 * 5
        total_salary = self.base_salary

        if self.experience > 3:
            counter = self.experience - 3
            while counter > 0:
                total_salary += bonus
                counter -= 1

        return total_salary


teacher = Teacher("Olga Ivanova", 35, False, 5)

teacher.introduce_myself()
print(f"Teacher's salary: {teacher.Salary()}")

def create_students():
    students = []
    students.append(Student("Aruuke", 17, False, {"Mathematics": [5, 4, 3], "Science": [4, 5, 5], "English": [4, 3, 5]}))
    students.append(Student("Aliya", 15, False, {"Mathematics": [4, 4, 4], "Science": [5, 5, 4], "English": [3, 4, 5]}))
    students.append(Student("Chyngyz", 12, False, {"Mathematics": [3, 4, 3], "Science": [4, 4, 5], "English": [5, 4, 4]}))
    return students


# Вызов функции и вывод информации о студентах
student_list = create_students()
for student in student_list:
    student.introduce_myself()