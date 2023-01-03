"""class Parent:
    print("single level")
    def method1(self):
        print("base class method")
class Childe1(Parent):
    def method2(self):
        print("child 1")
class Child2(Childe1):
    def method3(self):
        print("child 2")

obj = Child2()
obj.method1()
obj.method2()
obj.method3()"""

"""class A:
    print("Multiple level")
    def method1(self):
        print("base class method")
class B:
    def method2(self):
        print("Multiple 1")
class C(A,B):
    def method3(self):
        print("Multiple 1")

obj = C()
obj.method1()
obj.method2()
obj.method3()"""


"""class Multilevel0:
    print("Multilevel level")
    def method1(self):
        print("base class method")
class Multilevel1(Multilevel0):
    def method2(self):
        print("Multilevel 1")
class Multilevel2(Multilevel1):
    def method3(self):
        print("Multileve 2")

obj = Multilevel2()
obj.method1()
obj.method2()
obj.method3()"""

"""class A:
    print("Hierarchical")
    def method1(self):
        print("base class method")
class B(A):
    def method2(self):
        print("hello")
class C(A):
    def method3(self):
        print("hi")
obj = C()
obj.method1()
#obj.method2()
obj.method3()"""

class A:
    print("Hybrid level")
    def method1(self,name):
        print("Name is",name)
class B(A):
    def method2(self):
        print("call")
class C(A):
    def method3(self):
        print("calling")
class D(B,C):
    def method4(self):
        print("called")
print(issubclass(C, A))


obj = D()
obj.method1("don't know")
obj.method2()
obj.method3()
obj.method4()