def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anas = {}
    for i in strs:
        s = ''.join(sorted(i))
        if s in anas:
            anas[s].append(i)
        else:
            anas[s] = [i]
    return list(anas.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) 
# [["bat"],["nat","tan"],["ate","eat","tea"]]