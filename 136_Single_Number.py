def singleNumber(nums: list[int]) -> int:
        counts = dict().fromkeys(nums, 0)
        for i in nums:
            counts[i] += 1 
            if counts[i] == 2:
                del counts[i]
                
        return list(counts.keys())[0]