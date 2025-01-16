def findMaxAverage(nums: list[int], k: int) -> float:
        n = len(nums)
        curSum = 0

        for i in range(k):
            curSum += nums[i]
        
        largest = curSum / k

        for i in range(k, n):
            curSum += nums[i]
            curSum -= nums[i - k]

            largest = max(largest, curSum/k)
        return largest