def isAnagram(s, t):
    
    if len(s) != len(t):
        return False
    
    letters = {}
    
    for i in s:
        
        if i in letters:
            letters[i] += 1 
        else:
            letters[i] = 1 
    
    for i in t:
        
        if i in letters:
            letters[i] -= 1 
        else:
            return False
    
    for i in letters:
        if letters[i] != 0:
            return False
    
    return True



x = 'bbc'
y = 'bca'

check = isAnagram(x, y)
if check:
    print("is Anagram")
else:
    print("Not Anagram")