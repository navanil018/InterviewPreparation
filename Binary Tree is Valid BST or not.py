import sys

class Node:
    
    def __init__(self, val):
        
        self.val = val
        self.left = None
        self.right = None
    

def isValidBST(root):
    
    def isValidBST(root, mini, maxi):
        
        if root == None:
            return True
        
        if root.val < mini or root.val >= maxi:
            return False
        
        return isValidBST(root.left, mini, root.val) and isValidBST(root.right, root.val + 1, maxi)
    
    maximum = sys.maxsize
    minimum = - sys.maxsize - 1
    
    return isValidBST(root, minimum, maximum)

root = Node(5)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(8)

if isValidBST(root):
    print("Valid BST")
else:
    print("Not a valid BST")