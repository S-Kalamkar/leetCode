def majorityElement(nums: list[int]) -> int:
        currNum = None
        numCount = 0
        for n in nums:
            if numCount == 0:
                currNum = n
                numCount = 1
            elif n == currNum:
                numCount += 1
            else:
                numCount -= 1
        return currNum
