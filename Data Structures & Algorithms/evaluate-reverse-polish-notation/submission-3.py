class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      s1 = []
      temp = 0
      for c in tokens:
        if c in ['+', '-', '*','/']:
            a = s1.pop()
            b = s1.pop()
        if c == "+":
            temp = int(b)+int(a)
            s1.append(int(temp))
        elif c == "-":
            temp = int(b)-int(a)
            s1.append(int(temp))

        elif c == "*":
            temp = int(b)*int(a)
            s1.append(int(temp))
            print(s1)

        elif c == "/":
            temp = int(b)/int(a)
            s1.append(int(temp))
            print(s1)

        else:
            s1.append(int(c))
            print(s1)

      return s1[-1]
