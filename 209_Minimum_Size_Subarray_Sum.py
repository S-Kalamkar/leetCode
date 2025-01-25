def minSubArrayLen(target: int, nums: list[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        nums.insert(0, 0)
        
        minLen = 1000000
        l = 1
        for r in range(1, n + 1):
            while nums[r] - nums[l - 1] >= target:
                minLen = min(minLen, r - l + 1)
                l += 1
            
        return minLen if minLen != 1000000 else 0
        


