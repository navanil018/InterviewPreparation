'''
Kth most frequent recurrring string
'''
from collections import OrderedDict

def kthMostFrequent(s, k):
    
    store = OrderedDict()
    
    str1 = s.split(' ')
    
    
    for i in range(len(str1)):
        
        if str1[i] in store:
            
            store[str1[i]] += 1 
        else:
            store[str1[i]] = 1 
    
    res = []
    
    for i in store:
        
        if store[i] == k:
            res.append(i)
            
    #out = ' '.join(res)
    return res

check = "This is the best place in the town"
print(kthMostFrequent(check, 1))
    