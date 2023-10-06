'''program for single,multilevel,hierarchical'''
class Siva:
    def gold(wgl):
        print("price 5L")
    def car(wgl):
        print("price 3L")
class baby1(Siva):
    def bank(wgl):
        print("price 2L")
class baby2(Siva):
    def jewels(wgh):
        print("price 10L")
class gbaby(baby1):
    def abc(xyx):
        print("grandbaby")
gb=gbaby()
gb.gold()
gb.car()
gb.bank()
gb.abc()
b2=baby2()
b2.jewels()
