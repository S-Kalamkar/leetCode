def twoSum(numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers)-1

        while l <= r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            if target > numbers[l] + numbers[r]:
                l += 1
            else:
                r -= 1