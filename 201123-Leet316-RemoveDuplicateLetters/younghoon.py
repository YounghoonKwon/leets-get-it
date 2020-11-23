class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_idx = {}
        ans = []
        visited = set()
        
        for i, c in enumerate(s):
            last_idx[c] = i
            
        for i, c in enumerate(s):
            print(ans)
            print(visited)
            if c not in visited:
                while ans and c < ans[-1] and i < last_idx[ans[-1]]:
                    tail = ans.pop()
                    visited.remove(tail)
                ans.append(c)
                visited.add(c)
        return ''.join(ans)
