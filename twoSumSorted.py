def twoSum(numbers: list[int], target: int) -> list[int]:
    # lis = {}
    # n = len(numbers)

    # for i in range(n):
    #     lis[numbers[i]] = i
    
    # for i in range(n):
    #     val = target - numbers[i]
    #     if val in lis:
    #         return [i+1, lis[val]+1]
    
    l,r = 0, len(numbers)-1
    while(True):
        sum = numbers[l]+numbers[r]
        if(sum < target):
            l+=1
        elif(sum > target):
            r-=1
        else:
            return [l+1, r+1]
        
print(twoSum([2,7,11,15], 9)) # [1,2]