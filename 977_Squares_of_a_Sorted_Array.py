def sortedSquares(nums: list[int]) -> list[int]:
        nums.sort(key = lambda x: abs(x))
        return [i * i for i in nums]