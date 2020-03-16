class Node:
    
    def __init__(self, val):
        
        self.value = val
        self.left = None
        self.right = None


def sumTree(root):
    
    if root == None:
        return 0 
    
    old_val = root.value
    
    root.value = sumTree(root.left) + sumTree(root.right)
    
    return root.value + old_val

def printTree(root):
    
    if root == None:
        return

    printTree(root.left)
    print(root.value, end = " ")
    printTree(root.right)
    

if __name__ == '__main__':
    root = Node(10)  
    root.left = Node(-2)  
    root.right = Node(6)  
    root.left.left = Node(8)  
    root.left.right =  Node(-4)  
    root.right.left =  Node(7)  
    root.right.right =  Node(5) 
    
    sumTree(root)
    
    printTree(root)
    