def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n
    prefix = 1
    postfix = 1
    for i in range(n):
        answer[i] *= prefix
        prefix *= nums[i]
        r = n - 1 - i
        answer[r] *= postfix
        postfix *= nums[r]            
    return answer

print(productExceptSelf([1,2,3,4])) # [24,12,8,6]