class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_ = 0
        print('*', *strs)
        print('zip', list(zip(*strs)))
        for i in zip(*strs):
            print('i', i)
            if len(set(i)) == 1:
                len_ += 1
            else:
                break
        return strs[0][:len_] if len_ > 0 else ''
