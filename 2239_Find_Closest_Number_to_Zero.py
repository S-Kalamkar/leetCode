from time import perf_counter_ns
def findClosestNumber(nums: list[int]) -> int:
    closest = nums[0]
    for num in nums:
        if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
            closest = num
    return closest

         
start = perf_counter_ns()
print(findClosestNumber([-4,-2,1,4,8]))
print(f"{perf_counter_ns() - start} ns")
