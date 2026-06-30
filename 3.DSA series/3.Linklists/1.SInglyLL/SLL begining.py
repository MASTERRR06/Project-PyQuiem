class Node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next
class SLL:
    def __init__(self,head=None):
        self.head=head

    def insertbeg(self,value):
        temp=Node(value)
        temp.next=self.head
        self.head=temp


    def printll(self):
        if self.head is None:
            print("List is empty")
            return
        t1 = self.head
        while (t1.next != None):
            print(t1.data,end="->")
            t1 = t1.next
        print(t1.data)
obj=SLL()
n=int(input("How many elements to add?:"))
for i in range(n):
    value=int(input(f"Enter Element {i+1}:"))
    obj.insertbeg(value)
obj.printll()


