""" Problem 155. Min Stack """

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.container = []

    def push(self, x: int) -> None:
        self.container.append(x)

    def pop(self) -> None:
        self.container.pop(-1)

    def top(self) -> int:
        return self.container[-1]

    def getMin(self) -> int:
        return min(self.container)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()