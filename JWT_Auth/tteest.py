
def longestCommonPrefix(self, strs):
    prefix = ""
    first=strs[0]
    if not strs:
        return ""
    
    for i in first:
        prefix+=i
        print("************")
            
            
        for j in strs:
            if j.startswith(prefix)==False:
                return prefix[0:-1]
                
strs =  [""]

strs =  [""]
strs =  [""]
strs =  [""]

