import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i =0
        j = len(s)-1
        l = list(string.ascii_letters + string.digits)
        # print(l)
        while i<j:
            if s[i] not in l :
                i+=1
                continue
            if s[j] not in l :
                j-=1
                continue
            print(f"{s[i]} and {s[j]}")
            print(f"{i} and {j}")
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1

        return True
