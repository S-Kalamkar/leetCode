def longestConsecutive(nums: list[int]) -> int:
        nums = list(set(nums))
        nums.sort()

        n = len(nums)
        if n <= 1:
            return n

        counters = dict()
        counterNum = 0
        
        for i in range(n):
            try:
                if nums[i] + 1 == nums[i + 1]:
                    if counters.get(counterNum, 0) == 0:
                        counters[counterNum] = counters.get(counterNum, 0) + 2
                    else:
                        counters[counterNum] = counters.get(counterNum, 0) + 1
                else:
                    counterNum += 1
            except IndexError:
                try:
                    return (max(counters.values()))
                except ValueError:
                    return 1