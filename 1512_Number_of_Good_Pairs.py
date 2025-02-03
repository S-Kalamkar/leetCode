from collections import defaultdict

def numIdenticalPairs(nums: list[int]) -> int:
    numSet = defaultdict(list)
    n = len(nums)
    for i in range(n):
        numSet[nums[i]] += [i]
    numSet = dict(numSet)
    pairs = 0
    for i in numSet:
        n = len(numSet[i])
        if n == 1:
            continue
        else:
            for j in range(1, n):
                pairs += n - j
    return pairs
        