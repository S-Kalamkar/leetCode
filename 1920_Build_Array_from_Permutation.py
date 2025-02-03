def buildArray(nums: list[int]) -> list[int]:
        n = len(nums)
        return [nums[nums[i]] for i in range(n)]