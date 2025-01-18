def summaryRanges(nums: list[int]) -> list[str]:
    n = len(nums)
    if n == 0:
        return nums
    elif n == 1:
        return [f"{nums[0]}"]

    currRange = [nums[0], 'none']
    ranges = []

    for i in range(n - 1):
        if int(nums[i + 1]) == int(nums[i]) + 1:
            currRange[1] = nums[i + 1]
        else:
            if currRange[1] == 'none':
                ranges.append(f"{currRange[0]}")
            else:
                ranges.append(f"{currRange[0]}->{currRange[1]}")
            currRange = [nums[i + 1], 'none']
    if currRange[1] == 'none':
        ranges.append(f"{currRange[0]}")
    else:
        ranges.append(f"{currRange[0]}->{currRange[1]}")
    return ranges