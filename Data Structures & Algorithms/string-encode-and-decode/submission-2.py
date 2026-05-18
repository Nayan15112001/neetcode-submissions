class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            
            enc+=str(len(s))+'#'+s
        print(enc)
        return enc

    def decode(self, s: str) -> List[str]:
        i =0
        l = []
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            l.append(s[j+1:j+1+length])
            i = j+1+length
        return l