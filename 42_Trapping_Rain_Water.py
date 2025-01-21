def trap(height: list[int]) -> int:
    n = len(height)
    l, r = 0, n - 1
    total = 0
    lMax, rMax = 0, 0

    while l < r:
        if height[l] <= height[r]:
            if height[l] > lMax:
                lMax = height[l]
            else:
                total += lMax - height[l]
            l += 1
        else:
            if height[r] > rMax:
                rMax = height[r]
            else:
                total += rMax - height[r]
            r -= 1
    return total
