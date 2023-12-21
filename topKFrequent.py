from collections import defaultdict

def topKFrequent(nums: list[int], k: int) -> list[int]:
    numDict = defaultdict(lambda: 0)
    for i in nums:
        numDict[i] += 1
    numDict = sorted(numDict.items(), key=lambda x:x[1], reverse=True)
    lis = []
    for i,(a,_) in enumerate(numDict):
        if i==k:
            break
        lis.append(a)
        
    return lis

print(topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
print(topKFrequent([1], 1)) # [1]
print(topKFrequent([-1,2], 1)) # [1,2]