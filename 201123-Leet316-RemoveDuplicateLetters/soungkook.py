class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        myC=collections.Counter(s)
        print('myC', myC)
        res=[]
        seen=set()
        
        for c in s:
            
            while res and c<res[-1] and myC[res[-1]]>0 and c not in seen:
                x=res.pop()
                seen.discard(x)
                
            if c not in seen:    
                res.append(c)
                seen.add(c)
            myC[c]-=1
        return ''.join(res)   
