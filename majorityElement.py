def majorityElement(nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

# Test Cases:
nums = [3,2,3]
print(majorityElement(nums)) # 3
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums)) # 2