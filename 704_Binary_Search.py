def search(nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r: 
            i = (l + r) // 2
            if nums[i] == target:
                return i

            elif nums[i] > target:
                r = i - 1
            else:
                l = i + 1
        return -1