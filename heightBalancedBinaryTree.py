class Node:
    
    def __init__(self, x):
        
        self.val = x
        self.left = None
        self.right = None

class Height:
    def __init__(self):
        self.height = 0

def heightBalancedBinaryTree(root, height):
    
    lh = Height()
    rh = Height()
    
    if root is None:
        return True
    
    l = heightBalancedBinaryTree(root.left, lh)
    r = heightBalancedBinaryTree(root.right, rh)
    
    height.height = max(lh.height, rh.height) + 1
    
    if abs(lh.height - rh.height) <= 1: 
        return l and r 
  
    return False
        
height = Height()

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.left.left.left = Node(7) 


if heightBalancedBinaryTree(root, height): 
    print('Tree is balanced') 
else: 
    print('Tree is not balanced') 

