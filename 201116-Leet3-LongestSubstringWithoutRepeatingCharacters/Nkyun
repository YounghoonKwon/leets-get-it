class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)

        ch_dict = defaultdict(lambda : -1)
        cur_idx = 0
        length = len(s)
        cur_count = 0
        max_count = 1

        while cur_idx < length:
            ch = s[cur_idx]
            idx = ch_dict[ch]
            if idx == -1:
                ch_dict[ch] = cur_idx
                cur_count += 1
            else:
                max_count = max(cur_count, max_count)
                before_ch_idx = ch_dict[ch]
                start_idx = before_ch_idx + 1
                if before_ch_idx == (cur_idx - 1):
                    start_idx = cur_idx

                cur_idx = before_ch_idx
                cur_count = 0
                ch_dict = defaultdict(lambda: -1)
                if length - start_idx <= max_count:
                    break
            cur_idx += 1
        max_count = max(cur_count, max_count)
        return max_count
