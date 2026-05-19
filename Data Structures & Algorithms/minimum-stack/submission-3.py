class MinStack:

    def __init__(self):
        self.dataStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.dataStack.append(val)

        if (len(self.minStack) == 0):
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[-1], val))

    def pop(self) -> None:
        self.dataStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.dataStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
