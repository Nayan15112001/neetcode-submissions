class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stk = []
        star_stk = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                open_stk.append(i)
            elif c == '*':
                star_stk.append(i)
            else:
                if open_stk:
                    open_stk.pop()
                elif star_stk:
                    star_stk.pop()
                else:
                    return False
        
        while open_stk:
            if star_stk and open_stk[-1]<star_stk[-1]:
                open_stk.pop()
                star_stk.pop()
            else:
                return False
        
        return True
        

        