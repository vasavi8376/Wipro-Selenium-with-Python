#multiple inheritance is 2 parents and one chils class
class parent1:
    pass
class parent2:
    pass
class child(parent1, parent2):
    pass
class Father:
    def Driving(self):
        print("Father has the skills to drive")
class Mother:
     def Cooking(self):
         print("Mother has the skills to cook")
class Child(Father, Mother):
    def bothskills(self):
        print("Child has both skills of driving and cooking")
c = Child()
c.Driving()
c.Cooking()
c.bothskills()