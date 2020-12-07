class Solution:
    def nthUglyNumber(self, n: int) -> int:
        q = [1]
        seen = set()
        while True:
            num = heappop(q)
            if num in seen: continue
            seen.add(num)
            n -= 1
            if n == 0: return num
            for i in (2, 3, 5):
                heappush(q, num * i)