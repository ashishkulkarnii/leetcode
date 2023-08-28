class MyStack:

    def __init__(self):
        self.q1, self.q2 = [], []

    def push(self, x: int) -> None:
        self.q2.append(x)

    def pop(self) -> int:
        while len(self.q2) > 1:
            self.q1.append(self.q2.pop(0))
        res = self.q2.pop(0)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        return res

    def top(self) -> int:
        while len(self.q2) > 1:
            self.q1.append(self.q2.pop(0))
        res = self.q2.pop(0)
        self.q1.append(res)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        return res

    def empty(self) -> bool:
        return not self.q2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()