class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        q = [1]
        seen = set()
        while True:
            num = heappop(q)
            if num in seen: continue
            seen.add(num)
            n -= 1
            if n == 0: return num
            for i in primes:
                heappush(q, num * i)