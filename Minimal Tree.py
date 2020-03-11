class TreeNode:
    
    def __init__(self, x):
        
        self.val = x
        self.left = None
        self.right = None
        

def printing(node):
    
    if node != None:
        
        print(node.val)
        printing(node.left)
        printing(node.right)

def sortedArraytoBST(nums):
    
    if len(nums)==0:
        return None
    
    mid = len(nums)//2
    
    root = TreeNode(nums[mid])
    
    root.left = sortedArraytoBST(nums[:mid])
    
    root.right = sortedArraytoBST(nums[mid+1:])
    
    return root


n = [1,2,4,5,6,7,10]

forPrint = sortedArraytoBST(n)
printing(forPrint)


