""" Problem 232. Implement Queue using Stacks """

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if len(self.stack1) == 0:
            self.stack1.append(x)
        else: 
            # Step 1 pop all data to stack2
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop(-1))
            # step 2 stack1 append new data
            self.stack1.append(x)
            # step 3 pop all data back to stack 1
            for _ in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop(-1))


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack1.pop(-1)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()