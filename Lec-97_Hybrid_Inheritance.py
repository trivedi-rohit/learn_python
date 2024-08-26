class A:
    def  display(self):
        print("Display form A class.")

class B (A):
    def display(self):
        print("Display from B class.")

class C:
    def show (self):
        print("This is 'C' class.")
    
class D (B,C):
    def display (self):
        print("Display form 'D' class.")
    
d1 = D()
d1.display()
print(D.mro())

#******************************** Exercise********************************
class University():
    def __init__(self,uni_name):
        self.uni_name = uni_name
    def display(self):
        print(f'university : {self.uni_name}')
        
class Course(University):
    def __init__(self,uni_name,course_name):
        University.__init__(self,uni_name)
        self.course_name = course_name
    def display(self):
        print(f'Course : {self.course_name}')
        
class Branch(University):
    def __init__(self,uni_name,branch):
        University.__init__(self,uni_name)
        self.branch = branch
    def display(self):
        print(f'Branch : { self.branch} ')

class Student(Course,Branch):
    def __init__(self,uni_name,course_name,branch, student_name):
        Course.__init__(self,uni_name,course_name)
        Branch.__init__(self,uni_name,branch)
        self.student_name = student_name
    def display(self):
        print(f"Student : {self.student_name}")
        
class Faculty(Branch):
        def __init__(self,branch, faculty_name):
            Branch.__init__(self,branch,faculty_name)
            self.faculty_name = faculty_name
        def display(self):
            print(f"Faculty : {self.faculty_name}")
# u1 = University('ABC')   
# c1 = Course('ABC','B.Tech.') 
# b1 = Branch('ABC','ECE')        
student_1 = Student('AKTU','B.Tech.','ECE',"Rohit Trivedi")
faculty = Faculty("ECE","Dr. Pankaj Mishra")
# print(Student.mro())
student_1.display()
University.display(student_1)
Branch.display(student_1)
Faculty.display(faculty)
Course.display(student_1)