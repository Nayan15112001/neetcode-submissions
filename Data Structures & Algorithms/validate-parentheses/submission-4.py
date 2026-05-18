class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        st = []
        hmap = {')':'(','}':'{',']':'['}
        if len(s)==0:
            return True
        if len(s)==1:
            return False
        for i,ch in enumerate(s):
            if ch in ['(','[','{'] :
                st.append(ch)
                print(st)
            elif st and st[-1] == hmap[ch]:
                st.pop()
            else:
                return False

        

        return st == []