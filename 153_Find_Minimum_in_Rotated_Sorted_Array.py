def findMin(nums: list[int]) -> int:
        l, r = 0, len(nums)-1

        if l == r:
            return nums[0]

        while l < r:
            m = (l + r) // 2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        return nums[r]