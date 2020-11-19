class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_idx = 0
        for i in range(len(s)):
            current = s[i]
            print('current', s[i], i)
            
            p_idx = self.rcs(current, p_idx, p)
            print('ss', p_idx)
            if i == len(s)-1 and p_idx >= len(s):
                return True
            if p_idx < 0 or p_idx >= len(p):
                return False
        return True
    
    def rcs(self, current, p_idx, p):
        if p_idx >= len(p):
            return -1
        
        pattern = p[p_idx]
        print('pattern', pattern, p_idx)
        # there is .
        if pattern == '.':
            return p_idx + 1
        # there is *
        elif pattern == '*':
            # extend prior chractor with *
            case1 = self.rcs(current, p_idx-1, p)
            case2 = self.rcs(current, p_idx + 1, p)
            return case1, case2
        # there is only a letter
        else:
            # match
            if current == pattern:
                return p_idx+1
            else:
                # case of skip a charactor with * #compare current with charactor post *
                if '*' == p[p_idx+1]:
                    print('start to check whether skipping or wrong')
                    print(p[p_idx], p[p_idx+1])
                    print('result', self.rcs(current, p_idx+2, p))
                    return self.rcs(current, p_idx+2, p)
                else:
                    # in order to return False
                    return -1
        
