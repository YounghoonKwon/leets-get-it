class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Edge case
        if p is '':
            if s is '':
                return True
            else:
                return False
        # Simplified version:
        # if not p:
        #     return not s

        if s:
            first_char_match = p[0] in (s[0], '.')
        else:
            first_char_match = False
        # Simplified version:
        # first_char_match = bool(s) and p[0] in (s[0], '.')

        # len(p) < 2, p[1] will raise error
        if len(p) > 1 and p[1] == '*':
            """
            Try all possibilities:
            1) 0 occurrence, zero_ocr
            2) repeat is for one or more occurrence.
               This is bit subtle. The correct number of times of 
               deleting/ignoring/skipping will result in either case
               being True.
               e.g. s = 'aaa', p = 'a*a'
                    skips twice
                    s = 'a', p[2:] = 'a' -> True
               e.g. s = 'aab', p = 'a*b'
                    ...
                    s = 'b', p = 'a*b'
                    zero_ocr = isMatch('b', 'b') -> True
                    first_char_match = False
                    return zero_ocr, thus return True in the end
            """
            zero_ocr = self.isMatch(s, p[2:])
            if first_char_match:
                repeat = self.isMatch(s[1:], p)
                return zero_ocr or repeat
            return zero_ocr
            # Simplified version
            # return self.isMatch(s, p[2:]) \
            #        or (first_char_match and self.isMatch(s[1:], p))
        else:
            if first_char_match:
                return self.isMatch(s[1:], p[1:])
            else:
                return False
