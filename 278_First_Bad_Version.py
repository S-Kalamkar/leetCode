def firstBadVersion(n: int) -> int:
        l, r = 1, n
        
        while l < r:
            m = (l + r) // 2

            if isBadVersion(m): # type: ignore
                r = m 
            else:
                l = m + 1
        return r