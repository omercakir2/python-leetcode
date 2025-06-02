class Node:
    def __init__(self):
        self.data = 0
        self.next = None

    def __str__(self):
        if self.next:
            return f"Data :{self.data}-->{self.next.data}"
        else:
            return f"Data :{self.data}-->NULL"
    
class LinkedList:
    def __init__(self):
        self.head : Node = None
    def append(self,data):
        newnode = Node()
        newnode.data=data
        if not self.head:
            self.head=newnode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newnode
        
    def addBeginning(self,data):
        new = Node()
        new.data = data
        new.next = self.head
        self.head = new
        
    def getLength(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count
        
    def printList(self):
        curr = self.head
        print("Linked list content:")
        while curr:
            print(f"{curr.data}-->",end="")
            curr=curr.next
        print("None")
        
    def search(self,target):
        if not self.head:
            return
        curr = self.head
        while curr:
            if curr.data==target:
                print("Node has found",end=" ")
                print(curr)
            curr=curr.next
            
    def reverse(self):
        def f(curr : Node,prew : Node) -> Node:
            if not curr:
                return prew
            next = curr.next
            curr.next = prew
            return f(next,curr)
        self.head = f(self.head,None)
        
    def sortAscending(self):
        if not self.head or not self.head.next:
            return
        sorted : bool = False
        passes : int = 0
    
        len = self.getLength()
        
        while not sorted:
            curr = self.head
            sorted=True
            for i in range(0,len-passes-1,1):
                next : Node = curr.next
                if curr.data > next.data:
                    temp = curr.data
                    curr.data = next.data
                    next.data = temp
                    sorted = False
                curr = curr.next
            passes += 1
                
    def sortDecending(self):
        self.sortAscending()
        self.reverse()
    
        
        
list = LinkedList()
list.append(5)
list.append(15)
list.append(25)
list.append(35)
list.append(19)

list.printList()

list.reverse()

list.printList()

list.addBeginning(19)
list.printList()

list.sortDecending()
list.printList()

list.sortAscending()
list.printList()


list.search(19)


