def subsets(self, nums: list[int]) -> list[list[int]]:
    def recur(i, subset):
        if i >= len(nums):
            ans.append(subset[:])
            return
        
        recur(i + 1, subset[:])
        subset.append(nums[i])
        recur(i + 1, subset)

    ans = []
    recur(0, [])
    return ans