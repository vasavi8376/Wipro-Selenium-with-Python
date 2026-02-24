#we will write one function to  decorate another function
#wrapper function around the function are called decorators

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def vanillacake():
    print("I am the vanilla cake")
@make_pretty
def strawberrycake():
    print("I am the strawberry cake")
vanillacake()
strawberrycake()
