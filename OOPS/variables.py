#variables = used to store the data
#instance variables - global variables at class level
#local variables - inside the method only

#instance variable
class Student:

    #class variables
    school = "ravindra bharathi"
    def __init__(self, name, marks):
        self.name = name #instance variable or gobal variable
        self.marks = marks #instance variables or global variables
    def show(self):
        schoolcity = "Ongole"
        print(self.name, self.marks)
        print(schoolcity)
        print(self.school)

s1 = Student("bunny", 95)
s2 = Student("vasavi", 90)
s1.show()
s2.show()




