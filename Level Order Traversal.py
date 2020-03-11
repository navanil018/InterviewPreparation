class Node:
    
    def __init__(self, x):
        
        self.val = x
        self.left = None
        self.right = None

def levelOrderTraversal(root):
    
    if not root:
        return None
    
    queue = [(root,1)]
    d = {}
    result = []
    
    while queue:
        
        node, level = queue.pop(0)
        
        if node:
            
            if level in d:
                
                d[level].append(node.val)
                
            else:
                
                d[level] = [node.val]
                
            
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
    
    
    for k in d:
        result.append(d[k])
    
    return result
        
        


root = Node(10) 
root.left = Node(8) 
root.right = Node(2) 
root.left.left = Node(3) 
root.right.right = Node(90)


forPrint = levelOrderTraversal(root)
print(forPrint)


