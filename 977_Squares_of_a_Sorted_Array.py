def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x: abs(x))
        return [i * i for i in nums]