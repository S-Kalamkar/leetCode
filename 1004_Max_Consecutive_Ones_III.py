def longestOnes(nums: list[int], k: int) -> int:
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r] == 0:
                k -= 1
                
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1

        return r - l + 1