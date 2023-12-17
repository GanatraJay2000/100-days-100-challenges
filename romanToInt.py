def romanToInt(s: str) -> int:
    myMap = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    prev = ''
    sum=0
    for i in s[::-1]:
        if (i == 'I' and (prev=='X' or prev=='V')) or (i == 'X' and (prev=='L' or prev=='C')) or (i == 'C' and (prev=='D' or prev=='M')):
            sum = sum - myMap[i]
        else:
            sum = sum+myMap[i]
        prev = i

    return sum
        
print(romanToInt('MCMXCIV')) # 1994