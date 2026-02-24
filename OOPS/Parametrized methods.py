#default methods = built in methods, user defined methods - method name, method body
#parametrized methods- it allows the same method to behave differently for diff inputs

#parametrized methods (multiple parameter)
class calculator:
    def add(self, a, b):
        print(a + b)
c = calculator()
c.add(10, 20)
c.add(5, 7)
#default parameters
class test:
    def run(selfself, browser = "chrome"):
        print("running on", browser)
t  = test()
t.run()
t.run("Firefox")

# * args  parametrized methods
class Numbers:
    def total(self, *args):
        print(sum(args))

n = Numbers()
n.total(10, 20, 30)
n.total(10)
n.total(10, 60)