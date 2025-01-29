def permute(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    if n == 1:
        return [nums]

    ans = []

    def recur(remaining, perm):
        if len(remaining) == 0:
            ans.append(perm[:])
        else:
            for i in range(len(remaining)):
                tmp = remaining[i]
                remaining.remove(tmp)
                perm.append(tmp) 

                recur(remaining, perm)

                remaining.insert(i, tmp)
                perm.remove(perm[-1])
    recur(nums, [])
    return ans