class Person:
    def __init__(self, full_name, the_age, is_married):
        self.name= full_name
        self.age = the_age
        self.married = is_married
    def introduce_myself(self):
        marriage_status = "женат" if self.married else "неженат"
        print(f' Name: {self.name}, Age: {self.age} , Married_status {marriage_status}.')

class Student(Person):
    def __init__(self,  full_name, the_age, is_married, the_marks): #Добавила атрибут marks
        super().__init__(full_name, the_age, is_married)
        self.marks = the_marks
    def average_marks(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)  # Средняя оценка

class Teacher(Person):
    base_salary = 30000
    def __init__(self, full_name, the_age, is_married, the_experience):
        super().__init__(full_name, the_age, is_married)
        self.experience = the_experience

    def count_salary(self):
        if self.experience > 3:
            bonus = 0.05 * Teacher.base_salary *  (self.experience - 3)
        else:
            bonus = 0
        salary = Teacher.base_salary + bonus
        return salary

teacher_name = input('Введите имя учителя :')
teacher_age = int(input('Введите возраст учителя :'))
teacher_is_married = input('Женат no/yes? :')
teacher_experience = int(input('Ведите опыт работы учителя (в годах) :'))

teacher = Teacher(teacher_name, teacher_age, teacher_is_married, teacher_experience)
teacher.introduce_myself()
print(f'Зарплата учителя составляет:{teacher.count_salary()}')

def create_students():
    student = []
    student1 = Student("Константин Иванов", 16, False, {'Math': 5, 'English': 5, 'History': 5})
    student2 = Student("Анна Сидорова", 17, False, {'Math': 5, 'English': 4, 'History': 4})
    student3 = Student("Егор Петровский", 16, False, {'Math': 4, 'English': 5, 'History': 4})
    return [student1, student2, student3]

students = create_students()
for student in students:
    student.introduce_myself()
    print("Оценки по предметам:")
    for subject, mark in student.marks.items():
        print(f"{subject}: {mark}")
    print(f"Средняя оценка: {student.average_marks():.2}")



