def binaryGap(n: int) -> int:
        n = bin(n)[2:]
        gap = 0
        ans = 0
        for c in n:
            if c == '1':
                ans = max(ans, gap)
                gap = 0
            gap += 1
        return ans