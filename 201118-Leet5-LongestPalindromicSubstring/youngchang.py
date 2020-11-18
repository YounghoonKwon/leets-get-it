class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        
        answer = s[0]
        for i in range(length):
            dp[i][i] = 1
            if i < length - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = 2
                answer = s[i:i + 2]

        window_size = 2
        while window_size < length:
            r = 0
            while r + window_size < length:
                
                c = r + window_size
                if dp[r + 1][c - 1] > 0 and s[r] == s[c]:
                    dp[r][c] = dp[r + 1][c - 1] + 2
                    answer = s[r:c + 1]
                    
                r += 1
                    
            window_size += 1
            
        return answer