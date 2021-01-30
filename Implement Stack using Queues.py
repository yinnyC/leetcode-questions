"""Problem 225. Implement Stack using Queues """ 
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        len_queue1 = len(self.queue1)
        len_queue2 = len(self.queue2)
        
        for _ in range(len_queue1-1):
            self.queue2.append(self.queue1.pop(0))
        result = self.queue1.pop(0)
        self.queue1 = self.queue2
        self.queue2 = []
        return result

    def top(self) -> int:
        """
        Get the top element.
        """
        len_queue1 = len(self.queue1)
        len_queue2 = len(self.queue2)
        
        for _ in range(len_queue1-1):
            self.queue2.append(self.queue1.pop(0))
        result = self.queue1.pop(0)
        self.queue2.append(result)
        self.queue1 = self.queue2
        self.queue2 = []
        return result
            

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) ==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()