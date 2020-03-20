'''
String Compression
'''

def compress(s):
    
    result = ""
    count = 1
    
    for i in range(len(s)-1):
        
        if s[i] == s[i+1]:
            count += 1
            
        else:
            result += s[i] + str(count)
            count = 1
            
    result += s[i+1] + str(count) #edge case where we might miss the last repeatitive element, in this case e here.
    
    return result
        

print(compress("aabbcccddegggaaaaaa"))