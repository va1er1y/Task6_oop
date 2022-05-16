class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lect (self, lector, course, grade):
        if isinstance (lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
          
    def average_grades (self):
        sums = 0
        lens = 0
        for i in self.grades.values():
          sums += sum(i)
          lens += len(i)
        return sums/lens
  
    def __str__ (self):
        return f'Имя студента: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grades()} \nКурсы в процессе изучения: {" ".join(self.courses_in_progress)} \nЗавершенные курсы: {" ".join(self.finished_courses)}'

    def __lt__ (self, other):
        if not isinstance (other, self.__class__):
          print ('Таких нет в перечне.')
          return
        if self.average_grades() > other.average_grades():
          print (f'Средний бал у студента {self.name} больше.')
        else:
          print (f'Средний бал у студента {other.name} больше.')
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        
    
class Lecturer(Mentor):
  def __average_grades (self):
      return Student.average_grades (self)

  def __lt__ (self, other):
        if not isinstance (other, self.__class__):
          print ('Таких нет в перечне.')
          return
        if self.__average_grades() > other.__average_grades():
          print (f'Средний бал у лектора {self.name} больше.')
        else:
          print (f'Средний бал у лектора {other.name} больше.')
  
  def __str__ (self):
      return f'Имя лектора: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.__average_grades()}'
 
class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                
            else:
                student.grades[course] = [grade]
                
        else:
            return 'Ошибка'
          
    def __str__ (self):
        return f'Имя Ревьювера: {self.name} \nФамилия: {self.surname}'
  
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['java']

best_student2 = Student('Vova', 'Petechkin', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['java']

best_lector = Lecturer('Petr', 'Chvanov')
best_lector.courses_attached += ['Python']
best_lector.courses_attached += ['java']

best_lector2 = Lecturer('Fedor', 'Horochev')
best_lector2.courses_attached += ['Python']
best_lector2.courses_attached += ['java']

best_student.rate_lect (best_lector, 'Python', 10)
best_student.rate_lect (best_lector, 'java', 5)
best_student2.rate_lect (best_lector, 'Python', 8)
best_student2.rate_lect (best_lector, 'Python', 9)

best_student.rate_lect (best_lector2, 'Python', 10)
best_student.rate_lect (best_lector2, 'java', 10)
best_student2.rate_lect (best_lector2, 'Python', 10)
best_student2.rate_lect (best_lector2, 'Python', 10)

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['java']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw (best_student, 'java', 1)
cool_mentor.rate_hw (best_student, 'Python', 5)
cool_mentor.rate_hw (best_student, 'Python', 10)
cool_mentor.rate_hw (best_student2, 'java', 8)
cool_mentor.rate_hw (best_student2, 'Python', 8)

print (best_lector.__str__())
print ()
print (best_lector2.__str__())
print ()
print(best_student.__str__())
print ()
print(best_student2.__str__())
print ()
print (cool_mentor.__str__())
print ()
# best_student2 > best_student
# best_lector2 > best_lector

list_stud = []
list_stud.append(best_student) 
list_stud.append(best_student2)
course_stud = 'Python'

list_lect = []
list_lect.append(best_lector) 
list_lect.append(best_lector2)
course_lect = 'Python'

def student_grades_average (lists, name_course):
    all_grades = []
    for course in lists:
        all_grades.append(course.grades.get(name_course))
    sums = 0
    lens = 0
    for i in all_grades:
        sums += sum(i)
        lens += len(i)
    return print (f'Средняя оценка по курсу {name_course} составляет {sums/lens} баллов')

print ('Для студентов:')
student_grades_average (list_stud, course_stud)
print ('Для лекторов:')
student_grades_average (list_lect, course_lect)