class Node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next
class SLL:
    def __init__(self,head=None):
        self.head=head

    def deltion(self, value):
        # Case 1: The list is completely empty
        if (self.head == None):
            print("List is empty! Nothing to delete.")
            return

        # Case 2: The node to delete is the very first node (head)
        if self.head.data == value:
            self.head = self.head.next
            return

        # Case 3: The node to delete is somewhere in the middle or end
        t1 = self.head
        prev = None

        while (t1 != None):
            if t1.data == value:
                prev.next = t1.next  # Unlink the current node
                return  # Node deleted, exit the function
            prev = t1
            t1 = t1.next  # Safely advance to the next node

        print(f"Value {value} not found in the list.")

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
obj.printll()
n = int(input("How many elements do you want to delete?: "))
for i in range(n):
    value=int(input(f"Enter value to delete:"))

    obj.deltion(value)
obj.printll()


