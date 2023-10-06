'''default,parameter constructor'''
class Siva:
    def __init__(a):
        print("Default constructor")
    def __init__(a,b):
        super()
        print("Parameter constructor",b)
    def jeno(s):
        print("Test 1")
    def jeff(h):
        print("test 2")
s=Siva(10)
s.jeno()
s.jeff()
