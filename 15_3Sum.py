def threeSum(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    nums.sort()
    sols = set()
    for i in range(n):
        twosum = 0 - nums[i]
        l, r = i + 1, n - 1
        
        if nums[i] == nums[i-1] and i > 0:
            continue

        while l < r:
                
            check = nums[l] + nums[r]
            if check == twosum:
                sols.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
            elif check < twosum:
                l += 1
            else:
                r -= 1
    return [list(i) for i in sols]