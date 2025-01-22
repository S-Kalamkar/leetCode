from math import ceil
def minEatingSpeed(piles: list[int], h: int) -> int:
        def checkValidTime(n: int) -> bool:
            hours = 0
            for pile in piles:
                hours += ceil(pile / n)
            return hours <= h
        l, r = 1, max(piles)

        while l < r:
            m = (l + r) // 2
            if checkValidTime(m):
                r = m
            else:
                l = m + 1
        return r