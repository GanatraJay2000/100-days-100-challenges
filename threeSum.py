def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    lst = set()
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l,r = i+1, n-1
        sum=0
        while(l<r):
            a = nums[i]
            b = nums[l]
            c = nums[r]
            sum = a+b+c
            if (sum < 0) :
                l+=1
            elif(sum > 0):
                r-=1
            else:
                lst.add((a,b,c))
                l+=1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return lst


print(threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]