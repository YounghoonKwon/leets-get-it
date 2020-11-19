class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        
        #position on pattern
        p_idx = 0
        for i in range(len(s)):
            print('index of i :', i, s[i])
            current = s[i]
            
            # pattern should fit length of s
            if p_idx >= p_len:
                print('#1',"length doesn't match")
                return False
            pattern = p[p_idx]
            if pattern == '.':
                pattern = current
                
            if pattern == '*':
                # bring prior charactor in pattern
                p_idx -= 1
                pattern = p[p_idx]
                print('now', pattern)
                
                if pattern == '.':
                    pattern = current
            if True:
                # just compare charators
                if current == pattern:
                    print('#3', current, pattern)

                    p_idx += 1
                    
                    continue
                # no match
                else:
                    print('#4', current, pattern)

                    #check if * exists right after the charactor in pattern 
                    if p_idx+1 < p_len-1 and p[p_idx+1] == '*':
                        if current != p[p_idx+2]:
                            return False
                        print('#5', current, pattern)
                        p_idx += 3
                        
                        continue
                    else:
                        print('#6', current, pattern)
                        return False
        return True
