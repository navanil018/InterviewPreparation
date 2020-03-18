class Node:
    def __init__(self, val):
        
        self.val = val
        self.left = None
        self.right = None
    
def isSymmetric(root):
    
    if root == None:
        return True
    else:
        return symCheck(root.left, root.right)
    

def symCheck(node1, node2):
    
    if node1 == None and node2 == None:
        return True
    
    if node1 == None or node2 == None:
        return False
    
    if node1.val != node2.val:
        return False
    
    
    return symCheck(node1.left, node2.right) and symCheck(node1.right, node2.left)
    


root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4) 
root.right.left = Node(4) 
#root.right.right = Node(3) 

if isSymmetric(root):
    print("Symmetric")
else:
    print("Not Symmetric")

