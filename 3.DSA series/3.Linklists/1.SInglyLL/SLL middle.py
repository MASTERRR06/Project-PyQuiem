class Node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next
class SLL:
    def __init__(self,head=None):
        self.head=head

    def insertmid(self,value,loc):
        temp=Node(value)
        if (self.head == None):
            print("List is empty! Cannot insert.")
            return
        t1=self.head
        while(t1 != None):
            if(t1.data==loc):
                temp.next=t1.next
                t1.next=temp
                return
            t1=t1.next



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
obj.head = Node(10, Node(20, Node(30)))
n=int(input("How many elements to add?:"))
for i in range(n):
    value=int(input(f"Enter Element {i+1}:"))
    target = int(input(f"Enter after element {i + 1}:"))
    obj.insertmid(value,target)
obj.printll()


