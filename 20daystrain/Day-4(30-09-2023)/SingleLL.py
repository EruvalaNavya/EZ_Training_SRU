class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def create(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end="->")
            temp=temp.next
a=single()
a.create(20)
a.create(30)
a.add_front(60)
a.create(40)
a.display()
