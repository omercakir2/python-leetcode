from queue import Queue

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self,key):
        new = Node(key)
        if not self.root:
            self.root = new
            return
        parent = None
        temp = self.root
        while temp:
            parent = temp
            if key  > temp.key:
                temp = temp.right
            elif key < temp.key:
                temp = temp.left
            else:
                return
        if key < parent.key:
            parent.left = new
        else:
            parent.right = new     
    def inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.key, end=" ")
                _inorder(node.right)
        _inorder(self.root)
        print("")
        
    def bfs(self):
        if not self.root:
            print("Tree is empty")
            return
        
        print("Breath First Search Result:" ,end=" ")
        queue = Queue()
        queue.put(self.root)
        while not queue.empty():
            node : Node = queue.get()
            print(node.key,end=" ")
            
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
            
        print("")


my_tree = BST()


for i in range(1,10,1):
    my_tree.insert(i*10)
    
for i in range(1,20,2):
    my_tree.insert(i*5)

my_tree.inorder()

my_tree.bfs()

        