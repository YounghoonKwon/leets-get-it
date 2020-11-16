class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        is_Negative = False
        if x < 0:
            is_Negative = True

        x = str(abs(x))
        i = 1
        result = 0
        for ch in x:
            result += (int(ch) * i)
            i *= 10

        if is_Negative:
            result *= -1

        max_size = pow(2, 31)
        if -max_size < result < max_size - 1:
            return result
        else:
            return 0
