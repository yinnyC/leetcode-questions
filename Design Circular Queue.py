"""Problem 622. Design Circular Queue"""
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [None]*k
        self.head = 0
        self.tail = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.tail = (self.tail+1)% self.capacity
            self.queue[self.tail] = value
            self.size += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head = (self.head+1) % self.capacity
            self.size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else: 
            return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else: 
            return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()