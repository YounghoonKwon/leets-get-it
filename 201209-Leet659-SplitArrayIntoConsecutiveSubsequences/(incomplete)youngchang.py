class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        c = Counter(nums)
        
        def rm(dic, elem):
            dic[elem] -= 1
            if dic[elem] == 0:
                del dic[elem]
                
        def recur():
            if not c: return True
            st = min(c)
            res = False
            if st + 1 in c and st + 2 in c:
                rm(c, st)
                rm(c, st + 1)
                rm(c, st + 2)
                res |= recur()
                while st + 3 in c and not res:
                    rm(c, st + 3)
                    res |= recur()
                    st += 1
            
            return res
        
        return recur()