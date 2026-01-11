class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=""
        for i in s.lower():
            if i.isalnum():
                temp=temp+i
        print("temp",temp)
        return temp[::]==temp[::-1]
    
obj=Solution()
ans=obj.isPalindrome("A man, a plan, a canal: Panama")
print(ans)