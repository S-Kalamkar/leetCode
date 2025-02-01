def lastStoneWeight(stones: list[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            if x == y:
                if len(stones) == 0:
                    stones.append(0)
                continue
            else:
                stones.append(y - x)
                stones.sort()
        return stones[0]
        