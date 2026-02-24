#class is a blueprint or a template
#which describes the state / behaviour of its object
#data is put in variable
# behaviour is put in functions

class Student:
# data or the properties
    studentname = "Ravi"
    studentID = 677887

#self is used to access the attributes of teh class we have defines
#it is automatically loaded
#self represents teh instance of the class

#create a function to access the data
    def displaystudentdetails(self):
        print(self.studentname)
        print(self.studentID)

#create the object of class
a = Student()
a.displaystudentdetails()

