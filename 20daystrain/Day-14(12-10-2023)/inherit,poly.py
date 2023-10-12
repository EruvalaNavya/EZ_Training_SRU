#single inheritance
class cse:
    def fun1(s):
        print("parent")
class child(cse):
    def fun2(s):
        print("child")
a=cse()
b=child()
b.fun1()
b.fun2()
#Multiple inheritance
class grandf:
    def fun1(s):
        print("grandparent")
class parent(grandf):
    def fun2(s):
        print("child")
class child(parent):
    def fun3(s):
        print("child")
a=grandf()
b=parent()
c=child()
c.fun1()
c.fun2()
c.fun3()
#polymorphism(having multiple same methods in diff class,it can print last method value)
class cse:
    def fun1(s):
        print("parent")
class child(cse):
    def fun1(s):
        print("child")
a=cse()
b=child()
b.fun1()
#using super keyword we can parent class in child class
class cse:
    def fun1(s):
        print("parent")
class child(cse):
    def fun2(s):
        super().fun1()
        print("child")
a=cse()
b=child()
b.fun2()


