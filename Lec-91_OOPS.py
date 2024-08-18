# **** How add methods in class (what object will do)****
class Instructor:
    follower = 0
    def __init__(self,name, city):
        self.ins_name=name
        self.ins_city=city

    def display(self,subject):
        # self.subject_name = subject
        # print(f"Hello!,I am {self.ins_name} and I teach {self.subject_name}")
        print(f"Hello!,I am {self.ins_name} and I teach {subject}")

    def update_followers(self,followe_name):
        self.follower +=1

instructor_1 = Instructor('Rohit','Lucknow')
print(instructor_1.ins_name)
instructor_1.display('Python')
instructor_1.update_followers("Kunal")
print(instructor_1.follower)

instructor_2 = Instructor('Ashok','Delhi') # can't be left emptied
print((instructor_2.ins_name))
print(instructor_2.ins_city)
instructor_2.display('Java')
instructor_2.update_followers("Kunal")
instructor_2.update_followers("Raj")
print(instructor_2.follower)
