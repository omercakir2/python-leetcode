class binary_tree_node(object):
    def __init__(self,val=0,left_child=None,right_child=None):
        self.val = val
        self.right_child= right_child
        self.left_child= left_child
        
root =  binary_tree_node(19)
root.left_child = binary_tree_node(23)
print(root.left_child.val)
        