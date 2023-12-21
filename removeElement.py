def removeElement(nums: list[int], val: int) -> int:
    nums[:] = [num for num in nums if num!=val]
    return len(nums)

# Test Cases:
nums = [3,2,2,3]
val = 3
print(removeElement(nums, val)) # 2
print(nums) # [2,2]