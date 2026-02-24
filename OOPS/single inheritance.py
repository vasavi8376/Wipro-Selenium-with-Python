#single inheritance
#parent -----> child class - properties from parent class are acquired to child class
#create the object of the child classes to bring inheritance in  picture
class employee:
    def __init__(self, name, empid):
        self.name = name
        self.empid = empid

    def empdetails(self):
        print(self.name, self.empid)

#child class
class Manager(employee):

    def approve_leave(self):
        print("leave approved")
m = Manager("bunny", 45)
m.empdetails()
m.approve_leave()
