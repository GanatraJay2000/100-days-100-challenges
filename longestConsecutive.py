def longestConsecutive(nums: list[int]) -> int:
    if(len(nums)) <2:
        return len(nums)
    nums.sort()
    cur = nums[0]
    count = 1
    maxCount = 1
    
    for i in range(1,len(nums)):
        if nums[i]-cur == 0:
            continue
        if nums[i]-cur != 1:
            if(count>maxCount):
                maxCount = count
            count=1
        else:
            count+=1
        cur = nums[i]
        
    if(count>maxCount):
        maxCount = count
    return maxCount


print(longestConsecutive([100,4,200,1,3,2])) #4