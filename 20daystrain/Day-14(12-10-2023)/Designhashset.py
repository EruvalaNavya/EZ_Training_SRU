class MyHashSet:
    def __init__(self):
        self.s=set()
    def add(self,key)->None:
        self.s.add(key)
    def remove(self,key)->None:
        self.s.remove(key)
    def contains(self,key):
        if key in self.s:
            return True
        else:
            return False
obj=MyHashSet()
obj.add(10)
obj.add(20)
obj.add(30)
obj.remove(30)
res=obj.contains(20)
print(res)
