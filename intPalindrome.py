def intPalindrome(x: int) -> bool:
    if(x<0):
        return False   
    return x == int(str(x)[::-1])

print(intPalindrome(121)) # True