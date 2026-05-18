class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      s1 = []
      temp = 0
      for c in tokens:
        n = len(s1)
        if c == "+":
            temp = int(s1[n-2])+int(s1[n-1])
            s1.pop()
            s1.pop()
            s1.append(int(temp))
            print(s1)
        elif c == "-":
            temp = int(s1[n-2])-int(s1[n-1])
            s1.pop()
            s1.pop()
            s1.append(int(temp))
            print(s1)

        elif c == "*":
            temp = int(s1[n-2])*int(s1[n-1])
            s1.pop()
            s1.pop()
            s1.append(int(temp))
            print(s1)

        elif c == "/":
            temp = int(s1[n-2])/int(s1[n-1])
            s1.pop()
            s1.pop()
            s1.append(int(temp))
            print(s1)

        else:
            s1.append(int(c))
            print(s1)

      return s1[-1]
