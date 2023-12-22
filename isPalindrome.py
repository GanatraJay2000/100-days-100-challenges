def isPalindrome(s: str) -> bool:
    s = "".join([s.lower() for s in s if s.isalnum()])
    return s == s[::-1]
    # n=len(s)
    # l=0
    # r=n-1
    # while(l<r):
    #     if(s[l] != s[r]):
    #         return False
    #     l+=1;
    #     r-=1;
    # return True    

print(isPalindrome("A man, a plan, a canal: Panama")) #true