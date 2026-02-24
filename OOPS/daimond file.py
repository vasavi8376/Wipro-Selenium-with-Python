class A:
    def show(self):
        print("class A")
class B(A):
    pass
    #def show(self):
    #    print("class B")
class C(A):
    pass
    #def show(self):
    #    print("class c")
class D (B,C):
    pass
    #print("class D")

d = D()
d.show()
print(D.mro())