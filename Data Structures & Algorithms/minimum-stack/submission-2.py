class MinStack:

    def __init__(self):
        self.stk = []
        self.min = []

    def push(self, val: int) -> None:
        if len(self.min)>0 and val <= self.min[-1]:
            self.min.append(val)
        elif len(self.min)==0:
            self.min.append(val)
        return self.stk.append(val)

    def pop(self) -> None:
        if self.min[-1] == self.stk[-1]:
            self.min.pop()
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
