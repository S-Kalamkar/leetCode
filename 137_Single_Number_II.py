def singleNumber(nums: list[int]) -> int:
        counts = dict().fromkeys(nums, 0)
        for i in nums:
            counts[i] += 1 
        for i in counts:
            if counts[i] == 1:
                return i