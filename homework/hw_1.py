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
    def __init__(self, full_name, age, is_married, **marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def Average(self):
        average = sum(self.marks.values()) / len(self.marks.values())
        return f'average:{average}'

class Teacher(Person):
    base_salary = 30000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def introduce_myself(self):
        super().introduce_myself()
        print(f'I have {self.experience} years of experience.'
              f'\nMy salary is {self.Salary()}')

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


def create_students():
    first_st = Student("Арууке", 17, False, math=5, science=4, history=3)
    second_st = Student("Алибек", 20, True, math=5, science=5, history=4)
    third_st = Student("Алтынай", 19, False, math=3, science=3, history=5)
    student_list = [first_st, second_st, third_st]
    return student_list


student_list = create_students()
for student in student_list:
    student.introduce_myself()
    print(f"My marks: {student.marks}, {student.Average()}\n")