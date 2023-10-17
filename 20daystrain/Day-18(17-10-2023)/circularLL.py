class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
            self.tail.next=self.head
            self.head.prev=self.tail
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            new=node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
            self.tail.next=self.head
            self.head.prev=self.tail
    def deleteatbeg(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.head.prev=self.tail     
        self.tail.next=self.head
    def deleteend(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=self.head
    def printing(self):
        print(self.head.val,end="->")
        temp=self.head.next
        while(temp!=self.head):
            print(temp.val,end="->")
            temp=temp.next
    def reverse(self):
        curr=self.head
        while curr:
            curr.prev,curr.next=curr.next,curr.prev
            curr=curr.prev
        self.head,self.tail=self.tail,self.head
        while(temp!=self.head):
            print(temp.val,end="->")
            temp=temp.next
l=[2,4,6,7,9]
m=[5,1,3,8]
obj=dll()
for i in m:
    obj.insertatbeg(i)
obj.printing()
print()
for j in l:
    obj.insertatend(j)
obj.printing()
print()
obj.deleteatbeg()
obj.printing()
print()
obj.deleteend()
obj.printing()
obj.reverse()
obj.printing()