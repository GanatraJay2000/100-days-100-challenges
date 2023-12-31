# setup function for leetcode 2 sum problem. 

# Problem:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if(nums[i]+nums[j] == target):
                return [i,j]
    return -1


# Test Cases:   
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target)) # [0,1]
