def maxArea(height: list[int]) -> int:
        l, r = 0, len(height)-1
        largest = 0
        
        while l < r:
            w = r-l
            
            if height[l] > height[r]:
                h = height[r]
                r -= 1
            else:
                h = height[l]
                l += 1
            largest = max(largest, (w*h))
        return largest