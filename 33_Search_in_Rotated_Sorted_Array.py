def search(nums: list[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            m = (l + r) // 2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        minIndex = r
            
        if minIndex == 0:
            l, r = 0, n-1
        elif target >= nums[0] and target <= nums[minIndex - 1]:
            l, r = 0, minIndex - 1
        else:
            l, r = minIndex, n - 1
            
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1