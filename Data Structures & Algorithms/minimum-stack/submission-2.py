class MinStack:

    def __init__(self):
        self.arr = []
        self.minArr = []
        self.currentMin = math.inf

    def push(self, val: int) -> None:
        self.arr.append(val)
        if val < self.currentMin:
            self.currentMin = val
        self.minArr.append(self.currentMin)

    def pop(self) -> None:
        self.minArr.pop(-1)
        if len(self.minArr) > 0:
            self.currentMin = self.minArr[-1]
        else:
            self.currentMin = math.inf
        return self.arr.pop(-1)

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minArr[-1]
