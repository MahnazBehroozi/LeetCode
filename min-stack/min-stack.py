class MinStack:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.MinStack = []
​
    def push(self, x: int) -> None:
        self.MinStack.append(x)
​
    def pop(self) -> None:
        
        self.MinStack = self.MinStack[0:len(self.MinStack)-1]
        #print(self.MinStack)
​
    def top(self) -> int:
        return self.MinStack[len(self.MinStack)-1]
​
    def getMin(self) -> int:
        return min(self.MinStack)
​
​
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
