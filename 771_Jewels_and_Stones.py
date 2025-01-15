def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashSet = set(jewels)
        counter = 0
        for stone in stones:
            if stone in hashSet:
                counter += 1
        return counter