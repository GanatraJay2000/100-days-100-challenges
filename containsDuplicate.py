#  setup leetcode contains duplicate problem.

# Problem:
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums):
    lists = set()
    for i in nums:
        if i in lists:
            return True
        lists.add(i)

    return -1


# Test Cases:
nums = [1,2,3,1]
print(containsDuplicate(nums)) # True